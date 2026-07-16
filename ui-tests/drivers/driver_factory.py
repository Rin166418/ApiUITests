from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from config.config import HEADLESS, WINDOW_WIDTH, WINDOW_HEIGHT


def get_driver() -> webdriver.Chrome:
    """Создаёт настроенный Chrome WebDriver."""
    options = Options()

    if HEADLESS:
        options.add_argument("--headless=new")

    options.add_argument(f"--window-size={WINDOW_WIDTH},{WINDOW_HEIGHT}")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--lang=ru-RU")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()

    return driver
