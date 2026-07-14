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
