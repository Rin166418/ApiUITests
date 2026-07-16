from __future__ import annotations
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage


class CatalogPage(BasePage):
    """Page Object для каталога игр (страница /catalog/game-pc и результаты поиска)."""

    PRODUCT_TITLE_LINK = (
        By.XPATH,
        "//a[contains(@class,'ProductCard') and contains(@class,'title')]",
    )
    PRODUCT_CARD_WRAPPER = (
        By.XPATH,
        "//div[contains(@class,'ProductCard') and "
        "(contains(@class,'productCardWrapper') or .//a[contains(@class,'title')])]",
    )
    SHOW_MORE_BUTTON = (
        By.XPATH,
        "//button[contains(normalize-space(),'Показать ещё') or "
        "contains(normalize-space(),'Показать еще')]",
    )
    NO_RESULTS_TEXT_XPATH = (
        By.XPATH,
        "//*[contains(text(),'Здесь ничего нет') or contains(text(),'ничего не найдено')]",
    )

    def open_first_result(self) -> None:
        """Открыть первую карточку из списка результатов/каталога."""
        first_title = self.find_all(self.PRODUCT_TITLE_LINK)[0]
        self.scroll_to_element(first_title)
        first_title.click()

    def get_results_count(self) -> int:
        return len(self.driver.find_elements(*self.PRODUCT_TITLE_LINK))

    def wait_for_search_results(self, query: str, timeout: int = 15) -> None:
        """Дождаться, пока каталог применит поисковый запрос."""
        query = query.casefold()

        def search_finished(driver) -> bool:
            if driver.find_elements(*self.NO_RESULTS_TEXT_XPATH):
                return True
            titles = driver.find_elements(*self.PRODUCT_TITLE_LINK)
            return bool(titles) and all(query in el.text.casefold() for el in titles)

        WebDriverWait(self.driver, timeout).until(
            search_finished,
            message=f"Результаты поиска по запросу '{query}' не обновились",
        )

    def has_no_results_message(self) -> bool:
        return self.is_present(self.NO_RESULTS_TEXT_XPATH, timeout=5)

    def find_game_card_by_title(
        self, title: str, max_scrolls: int = 60, scroll_step_px: int = 1200
    ) -> WebElement | None:
        """Ищет карточку по названию, подгружая каталог при необходимости."""
        normalized_title = title.casefold()
        unchanged_count = 0

        for _ in range(max_scrolls):
            titles = self.driver.find_elements(*self.PRODUCT_TITLE_LINK)
            for el in titles:
                try:
                    if normalized_title in el.text.strip().casefold():
                        self.scroll_to_element(el)
                        return el
                except StaleElementReferenceException:
                    break

            buttons = self.driver.find_elements(*self.SHOW_MORE_BUTTON)
            old_count = len(titles)
            old_height = self.driver.execute_script("return document.body.scrollHeight")

            if buttons:
                button = buttons[0]
                self.scroll_to_element(button)
                self.driver.execute_script("arguments[0].click();", button)
            else:
                self.driver.execute_script(f"window.scrollBy(0, {scroll_step_px});")

            try:
                WebDriverWait(self.driver, 3).until(
                    lambda driver: (
                        len(driver.find_elements(*self.PRODUCT_TITLE_LINK)) > old_count
                        or driver.execute_script("return document.body.scrollHeight")
                        > old_height
                    )
                )
                unchanged_count = 0
            except TimeoutException:
                unchanged_count += 1
                if unchanged_count >= 3:
                    break

        return None
