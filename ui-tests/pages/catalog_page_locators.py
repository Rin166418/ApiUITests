"""
Локаторы для CatalogPage (каталог игр).
"""
from selenium.webdriver.common.by import By


class CatalogPageLocators:
    """Локаторы для страницы каталога игр"""
    
    # Поисковая строка
    SEARCH_INPUT = (By.XPATH, "//input[@placeholder='Поиск по названиям' or @type='search']")
    
    # Кнопка поиска / клавиша Enter используется вместо кнопки
    SEARCH_BUTTON = (By.XPATH, "//button[@type='submit' and contains(text(), 'Поиск')]")
    
    # Карточка игры в результатах поиска (первая)
    FIRST_GAME_CARD = (By.XPATH, "//div[contains(@class, 'game-card') or contains(@class, 'product-card')]//a")
    
    # Карточка игры по названию (для поиска без использования поля поиска)
    GAME_CARD_BY_TITLE = "//div[contains(@class, 'game-card') or contains(@class, 'product-card')]//a[contains(., '{title}')]"
    
    # Контейнер со списком карточек
    GAMES_LIST = (By.XPATH, "//div[@class='products-list' or contains(@class, 'products')]")
