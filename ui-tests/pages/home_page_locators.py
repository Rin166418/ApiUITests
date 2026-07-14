"""
Локаторы для HomePage.
"""
from selenium.webdriver.common.by import By


class HomePageLocators:
    """Локаторы для главной страницы igrovoy.rt.ru"""
    
    # Меню "Игры" в верхней навигации
    GAMES_MENU = (By.XPATH, "//a[contains(@class, 'header-nav__item') and contains(., 'Игры')]")
    
    # Кнопка "PC" в выпадающем меню
    PC_CATEGORY = (By.XPATH, "//a[contains(@class, 'dropdown') and contains(., 'PC')]")
