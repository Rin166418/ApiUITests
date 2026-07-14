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
        Вводит текст в поисковую строку и нажимает Enter.
        
        :param query: название игры для поиска
        """
        self.send_keys(CatalogPageLocators.SEARCH_INPUT, query)
        # Нажимаем Enter для поиска
        search_input = self.find_element(CatalogPageLocators.SEARCH_INPUT)
        search_input.submit()
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
