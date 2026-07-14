"""
CatalogPage — страница каталога игр (PC)
"""
import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.catalog_page_locators import CatalogPageLocators


class CatalogPage(BasePage):
    """
    Page Object для страницы каталога игр.
    """
    
    def search_game(self, query: str):
        """
        Вводит текст в поисковую строку и нажимает кнопку "Найти" или Enter.
        
        :param query: название игры для поиска
        """
        self.send_keys(CatalogPageLocators.SEARCH_INPUT, query)
        # Клик на кнопку "Найти"
        self.click(CatalogPageLocators.SEARCH_BUTTON)
        # Даём время на загрузку результатов
        time.sleep(2)
    
    def find_game_card_by_title(self, title: str):
        """
        Находит карточку игры по названию без использования поиска.
        Скроллит список, пока не найдёт карточку с нужным названием.
        
        :param title: названием игры для поиска
        :return: WebElement — найденная карточка
        """
        # Создаём динамический локатор для поиска по названию
        locator = (By.XPATH, CatalogPageLocators.GAME_CARD_BY_TITLE.format(title=title))
        
        # Пытаемся найти элемент, скроллируя вниз
        for attempt in range(10):  # макс 10 попыток скролла
            try:
                return self.find_element(locator)
            except:
                # Если не найдена, скроллим вниз
                self.scroll_to_bottom()
                time.sleep(1)
        
        raise Exception(f"Игра '{title}' не найдена после прокрутки списка")
    
    def open_first_result(self):
        """
        Кликает на первую карточку в результатах поиска.
        Открывает страницу с информацией об игре.
        """
        self.click(CatalogPageLocators.FIRST_GAME_CARD)
    
    def open_first_result_via_details_button(self):
        """
        Открывает первую карточку через кнопку "Подробнее" (hover -> click).
        Альтернативный способ открытия карточки.
        """
        # Наводим курсор на первую карточку
        self.hover(CatalogPageLocators.FIRST_GAME_CARD)
        time.sleep(0.5)  # Даём время на отображение кнопки "Подробнее"
        # Кликаем на "Подробнее"
        self.click(CatalogPageLocators.FIRST_GAME_CARD_DETAILS_BUTTON)
    
    def is_no_results_displayed(self) -> bool:
        """
        Проверяет, отображается ли сообщение "ничего не найдено".
        
        :return: True если сообщение видно, False если нет
        """
        return self.is_element_visible(CatalogPageLocators.NO_RESULTS_MESSAGE)
