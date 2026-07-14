"""
HomePage — главная страница igrovoy.rt.ru
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.home_page_locators import HomePageLocators


class HomePage(BasePage):
    """
    Page Object для главной страницы.
    """
    
    def hover_games_menu(self):
        """
        Наводит курсор на пункт меню "Игры" в верхней навигации.
        """
        self.hover(HomePageLocators.GAMES_MENU)
    
    def click_pc_category(self):
        """
        Кликает на "PC" в выпадающем меню "Игры".
        Переходит на страницу каталога PC-игр.
        """
        self.click(HomePageLocators.PC_CATEGORY)
    
    def open_game_card_by_title(self, title: str):
        """
        Открывает карточку игры на главной странице по названию.
        
        :param title: название игры
        """
        locator = (By.XPATH, HomePageLocators.GAME_CARD_BY_TITLE.format(title=title))
        self.scroll_to_bottom()
        self.click(locator)
