from __future__ import annotations
import allure
from selenium.common.exceptions import (
    TimeoutException,
    StaleElementReferenceException,
    ElementClickInterceptedException,
)
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from config.config import BASE_URL, DEFAULT_TIMEOUT


class BasePage:
    """Общие действия для страниц сайта."""

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, DEFAULT_TIMEOUT)

    def open(self, path: str = "") -> None:
        url = f"{BASE_URL}{path}"
        with allure.step(f"Открыть страницу: {url}"):
            self.driver.get(url)

    def find(self, locator: tuple) -> WebElement:
        with allure.step(f"Найти элемент: {locator}"):
            return self.wait.until(
                EC.presence_of_element_located(locator),
                message=f"Элемент не найден за {DEFAULT_TIMEOUT}с: {locator}",
            )

    def find_all(self, locator: tuple) -> list[WebElement]:
        with allure.step(f"Найти все элементы: {locator}"):
            self.wait.until(
                EC.presence_of_element_located(locator),
                message=f"Элементы не найдены за {DEFAULT_TIMEOUT}с: {locator}",
            )
            return self.driver.find_elements(*locator)

    def find_clickable(self, locator: tuple) -> WebElement:
        with allure.step(f"Дождаться кликабельности элемента: {locator}"):
            return self.wait.until(
                EC.element_to_be_clickable(locator),
                message=f"Элемент не стал кликабельным за {DEFAULT_TIMEOUT}с: {locator}",
            )

    def find_visible(self, locator: tuple) -> WebElement:
        with allure.step(f"Дождаться видимости элемента: {locator}"):
            return self.wait.until(
                EC.visibility_of_element_located(locator),
                message=f"Элемент не стал видимым за {DEFAULT_TIMEOUT}с: {locator}",
            )

    def is_present(self, locator: tuple, timeout: int = 5) -> bool:
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def is_visible(self, locator: tuple, timeout: int = 5) -> bool:
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def click(self, locator: tuple) -> None:
        with allure.step(f"Кликнуть по элементу: {locator}"):
            element = self.find_clickable(locator)
            try:
                element.click()
            except (ElementClickInterceptedException, StaleElementReferenceException):
                element = self.find_clickable(locator)
                self.driver.execute_script("arguments[0].click();", element)

    def hover(self, locator: tuple) -> None:
        with allure.step(f"Навести курсор на элемент: {locator}"):
            element = self.find_visible(locator)
            ActionChains(self.driver).move_to_element(element).perform()

    def send_keys(self, locator: tuple, text: str, clear_first: bool = True) -> None:
        with allure.step(f"Ввести текст '{text}' в поле: {locator}"):
            element = self.find_visible(locator)
            if clear_first:
                element.clear()
            element.send_keys(text)

    def get_text(self, locator: tuple) -> str:
        with allure.step(f"Получить текст элемента: {locator}"):
            return self.find_visible(locator).text.strip()

    def get_texts(self, locator: tuple) -> list[str]:
        with allure.step(f"Получить тексты элементов: {locator}"):
            return [el.text.strip() for el in self.find_all(locator)]

    def get_attribute(self, locator: tuple, attribute: str) -> str | None:
        with allure.step(f"Получить атрибут '{attribute}' элемента: {locator}"):
            return self.find(locator).get_attribute(attribute)

    def scroll_to_element(self, locator_or_element) -> None:
        with allure.step("Прокрутить страницу к элементу"):
            element = (
                locator_or_element
                if isinstance(locator_or_element, WebElement)
                else self.find(locator_or_element)
            )
            self.driver.execute_script(
                "arguments[0].scrollIntoView({block: 'center', behavior: 'instant'});",
                element,
            )

    def scroll_to_bottom(self) -> None:
        with allure.step("Прокрутить страницу в самый низ"):
            last_height = self.driver.execute_script("return document.body.scrollHeight")
            while True:
                self.driver.execute_script(
                    "window.scrollTo(0, document.body.scrollHeight);"
                )
                self.wait_for_seconds(0.5)
                new_height = self.driver.execute_script(
                    "return document.body.scrollHeight"
                )
                if new_height == last_height:
                    break
                last_height = new_height

    def switch_to_new_tab(self) -> None:
        with allure.step("Переключиться на новую вкладку"):
            self.wait.until(lambda d: len(d.window_handles) > 1)
            self.driver.switch_to.window(self.driver.window_handles[-1])

    def close_current_tab_and_return(self) -> None:
        with allure.step("Закрыть текущую вкладку и вернуться на предыдущую"):
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])

    @staticmethod
    def wait_for_seconds(seconds: float) -> None:
        import time
        time.sleep(seconds)

    def wait_for_element_to_disappear(self, locator: tuple, timeout: int = 10) -> None:
        with allure.step(f"Дождаться исчезновения элемента: {locator}"):
            WebDriverWait(self.driver, timeout).until_not(
                EC.presence_of_element_located(locator)
            )

    @staticmethod
    def price_text_to_int(price_text: str) -> int:
        """
        Универсальный парсер цены из текста вида '699 ₽', '699р.', '699 руб.'
        в целое число рублей.
        """
        digits = "".join(ch for ch in price_text if ch.isdigit())
        if not digits:
            raise ValueError(f"Не удалось извлечь цену из текста: '{price_text}'")
        return int(digits)
