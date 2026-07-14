"""
Централизованная конфигурация для UI-тестов.
"""
import os
from pathlib import Path

# Базовый URL целевого сайта
BASE_URL = "https://igrovoy.rt.ru/"

# Таймауты (в секундах)
EXPLICIT_WAIT_TIMEOUT = 10
PAGE_LOAD_TIMEOUT = 15
IMPLICIT_WAIT_TIMEOUT = 5

# Настройки браузера
HEADLESS = os.getenv("HEADLESS", "False").lower() == "true"
BROWSER_WIDTH = 1920
BROWSER_HEIGHT = 1080

# Путь для Allure отчётов
ALLURE_RESULTS_DIR = Path(__file__).parent.parent / "allure-results"
ALLURE_RESULTS_DIR.mkdir(exist_ok=True)

# Путь для скриншотов
SCREENSHOTS_DIR = Path(__file__).parent.parent / "screenshots"
SCREENSHOTS_DIR.mkdir(exist_ok=True)
