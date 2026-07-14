"""
Локаторы для GameCardPage (страница карточки игры).
"""
from selenium.webdriver.common.by import By


class GameCardPageLocators:
    """Локаторы для страницы карточки игры"""
    
    # Цена товара
    PRICE = (By.XPATH, "//span[@class='price' or contains(@class, 'game-price')]")
    
    # Минимальные требования
    MIN_REQUIREMENTS = (By.XPATH, "//div[contains(@class, 'requirements') or contains(., 'Минимальные')]")
    
    # ОС в требованиях
    OS_REQUIREMENT = (By.XPATH, "//span[contains(text(), 'ОС') or contains(text(), 'OS')]//following-sibling::span")
    
    # Процессор в требованиях
    CPU_REQUIREMENT = (By.XPATH, "//span[contains(text(), 'Процессор') or contains(text(), 'CPU')]//following-sibling::span")
    
    # ОЗУ в требованиях
    RAM_REQUIREMENT = (By.XPATH, "//span[contains(text(), 'ОЗУ') or contains(text(), 'RAM')]//following-sibling::span")
    
    # Видеокарта в требованиях
    GPU_REQUIREMENT = (By.XPATH, "//span[contains(text(), 'Видеокарта') or contains(text(), 'GPU')]//following-sibling::span")
    
    # Жёсткий диск в требованиях
    STORAGE_REQUIREMENT = (By.XPATH, "//span[contains(text(), 'Жёсткий диск') or contains(text(), 'Storage')]//following-sibling::span")
    
    # Блок "Скачать игру"
    DOWNLOAD_BLOCK = (By.XPATH, "//div[contains(@class, 'download') or contains(text(), 'Скачать')]")
    
    # Ссылка на Google Play
    GOOGLE_PLAY_LINK = (By.XPATH, "//a[contains(@href, 'play.google.com') or contains(text(), 'Google Play')]")
    
    # Ссылка на App Store
    APP_STORE_LINK = (By.XPATH, "//a[contains(@href, 'apps.apple.com') or contains(text(), 'App Store')]")
