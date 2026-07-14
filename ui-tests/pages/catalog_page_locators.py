"""
Локаторы для CatalogPage (каталог игр).
"""
from selenium.webdriver.common.by import By


class CatalogPageLocators:
    """Локаторы для страницы каталога игр"""
    
    # Поисковая строка
    SEARCH_INPUT = (By.XPATH, "//input[@placeholder='Поиск' or contains(@placeholder, 'Поиск')]")
    
    # Кнопка "Найти" рядом с поиском
    SEARCH_BUTTON = (By.XPATH, "//button[contains(text(), 'Найти')]")
    
    # Контейнер со списком карточек игр
    GAMES_LIST = (By.XPATH, "//div[contains(@class, 'product') or contains(@class, 'game-card')]")
    
    # Первая карточка в результатах поиска
    FIRST_GAME_CARD = (By.XPATH, "(//div[contains(@class, 'product')])[1]")
    
    # Кнопка "Подробнее" (appears on hover) на первой карточке
    FIRST_GAME_CARD_DETAILS_BUTTON = (By.XPATH, "(//div[contains(@class, 'product')])[1]//button[contains(text(), 'Подробнее')]")
    
    # Кнопка "Подробнее" - generic для hover
    GAME_CARD_DETAILS_BUTTON = (By.XPATH, ".//button[contains(text(), 'Подробнее')]")
    
    # Карточка игры по названию (для поиска без использования поля поиска)
    GAME_CARD_BY_TITLE = "//div[contains(@class, 'product')]//h3[contains(., '{title}')]//ancestor::div[contains(@class, 'product')]"
    
    # Сообщение "ничего не найдено"
    NO_RESULTS_MESSAGE = (By.XPATH, "//text()[contains(., 'ничего не найдено')] | //div[contains(text(), 'По заданным')]")
