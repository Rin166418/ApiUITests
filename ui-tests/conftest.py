"""
Конфигурация pytest. Фикстуры и хуки для управления браузером и Allure отчётами.
"""
import pytest
from pathlib import Path
from datetime import datetime

from drivers.driver_factory import get_driver
from config.config import SCREENSHOTS_DIR


@pytest.fixture(scope="function")
def driver():
    """
    Фикстура для инициализации WebDriver перед каждым тестом.
    Закрывает браузер после теста.
    """
    browser_driver = get_driver()
    yield browser_driver
    browser_driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Хук для создания скриншотов при падении теста.
    """
    outcome = yield
    rep = outcome.get_result()
    
    # Если тест прошёл неудачно и у теста есть фикстура driver
    if rep.failed and "driver" in item.fixturenames:
        driver = item.funcargs.get("driver")
        if driver:
            # Создаём скриншот
            screenshot_path = SCREENSHOTS_DIR / f"{item.name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            driver.save_screenshot(str(screenshot_path))
            
            # Добавляем скриншот в Allure отчёт
            try:
                import allure
                allure.attach.file(
                    str(screenshot_path),
                    name=f"screenshot_{item.name}",
                    attachment_type=allure.attachment_type.PNG
                )
            except ImportError:
                pass
