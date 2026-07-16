import allure
import pytest

from drivers.driver_factory import get_driver


@pytest.fixture(scope="function")
def driver():
    """Создаёт браузер для теста и закрывает его после выполнения."""
    drv = get_driver()
    yield drv
    drv.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Добавляет скриншот и URL в Allure при падении теста."""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver is not None:
            try:
                allure.attach(
                    driver.get_screenshot_as_png(),
                    name="screenshot_on_failure",
                    attachment_type=allure.attachment_type.PNG,
                )
                allure.attach(
                    driver.current_url,
                    name="current_url",
                    attachment_type=allure.attachment_type.TEXT,
                )
            except Exception:
                pass
