"""
Локаторы для GameCardPage (страница карточки игры).
"""
from selenium.webdriver.common.by import By


class GameCardPageLocators:
    """Локаторы для страницы карточки игры"""
    
    # Цена товара на странице карточки
    PRICE = (By.XPATH, "//span[contains(text(), '₽') or contains(text(), 'Р')] | //div[contains(@class, 'price')]//span")
    
    # Минимальные требования (блок с требованиями)
    MIN_REQUIREMENTS = (By.XPATH, "//h3[contains(text(), 'Минимальные')] | //div[contains(@class, 'requirements')]")
    
    # ОС в требованиях
    OS_REQUIREMENT = (By.XPATH, "//td[contains(text(), 'ОС') or contains(text(), 'OS')]//following-sibling::td")
    
    # Процессор в требованиях
    CPU_REQUIREMENT = (By.XPATH, "//td[contains(text(), 'Процессор') or contains(text(), 'CPU')]//following-sibling::td")
    
    # ОЗУ в требованиях
    RAM_REQUIREMENT = (By.XPATH, "//td[contains(text(), 'ОЗУ') or contains(text(), 'RAM')]//following-sibling::td")
    
    # Видеокарта в требованиях
    GPU_REQUIREMENT = (By.XPATH, "//td[contains(text(), 'Видеокарта') or contains(text(), 'GPU')]//following-sibling::td")
    
    # Жёсткий диск в требованиях
    STORAGE_REQUIREMENT = (By.XPATH, "//td[contains(text(), 'Жёсткий диск') or contains(text(), 'Storage') or contains(text(), 'Место')]//following-sibling::td")
    
    # Блок "Скачать игру"
    DOWNLOAD_BLOCK = (By.XPATH, "//h3[contains(text(), 'Скачать')] | //div[contains(text(), 'Скачать')]")
    
    # Ссылка на Google Play
    GOOGLE_PLAY_LINK = (By.XPATH, "//a[contains(@href, 'play.google.com')] | //a[contains(text(), 'Google Play')]")
    
    # Ссылка на App Store
    APP_STORE_LINK = (By.XPATH, "//a[contains(@href, 'apps.apple.com')] | //a[contains(text(), 'App Store')]")
