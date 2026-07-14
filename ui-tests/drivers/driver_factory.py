"""
Фабрика для инициализации и управления WebDriver.
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from config.config import HEADLESS, BROWSER_WIDTH, BROWSER_HEIGHT, EXPLICIT_WAIT_TIMEOUT, PAGE_LOAD_TIMEOUT


def get_driver():
    """
    Инициализирует и возвращает Chrome WebDriver.
    
    :return: selenium.webdriver.Chrome
    """
    chrome_options = Options()
    
    if HEADLESS:
        chrome_options.add_argument("--headless=new")
    
    # Отключаем sandbox для стабильности в CI/CD
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    # Устанавливаем разрешение окна
    chrome_options.add_argument(f"--window-size={BROWSER_WIDTH},{BROWSER_HEIGHT}")
    
    # Отключаем различные предупреждения и логи
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)
    
    # Инициализируем драйвер с webdriver-manager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    # Устанавливаем таймауты
    driver.set_page_load_timeout(PAGE_LOAD_TIMEOUT)
    driver.set_script_timeout(EXPLICIT_WAIT_TIMEOUT)
    
    return driver
