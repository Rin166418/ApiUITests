from __future__ import annotations
from selenium.webdriver.common.by import By

from pages.base_page import BasePage

# Соответствие подписи в системных требованиях -> ключ в словаре результата
_REQ_LABEL_TO_KEY = {
    "Операционная система": "os",
    "Процессор": "cpu",
    "Оперативная память": "ram",
    "Видеокарта": "gpu",
    "Жесткий диск": "storage",
}


class GameCardPage(BasePage):
    """Page Object для карточки отдельной игры (/catalog/game-pc/{id}/{slug})."""

    PRICE = (
        By.XPATH,
        "//span[contains(@class,'rt-Text') and contains(text(),'₽') "
        "and not(contains(@class,'crossed-price'))]",
    )
    MIN_REQUIREMENTS_TITLE = (
        By.XPATH,
        "//h4[contains(@class,'SystemRequirements-module-scss-module__NEb1Ga__title') "
        "and normalize-space(text())='Минимальные']",
    )
    REQ_ITEM_CSS = "span[class*='SystemRequirements'][class*='item']"

    def get_price(self) -> str:
        """Возвращает текст цены как есть, например '1 499 ₽'."""
        return self.get_text(self.PRICE)

    def get_price_rub(self) -> int:
        """Возвращает цену в виде целого числа рублей."""
        return self.price_text_to_int(self.get_price())

    def get_min_requirements(self) -> dict:
        """
        Возвращает словарь минимальных системных требований:
        {'os': ..., 'cpu': ..., 'ram': ..., 'gpu': ..., 'storage': ...}
        """
        title_el = self.find(self.MIN_REQUIREMENTS_TITLE)
        wrapper = title_el.find_element(By.XPATH, "..")
        items = wrapper.find_elements(By.CSS_SELECTOR, self.REQ_ITEM_CSS)

        result: dict[str, str] = {}
        for item in items:
            text = item.text.strip()
            for label, key in _REQ_LABEL_TO_KEY.items():
                if label in text and ":" in text:
                    result[key] = text.split(":", 1)[1].strip()
                    break
        return result
