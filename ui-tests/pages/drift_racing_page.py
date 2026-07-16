from __future__ import annotations
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class DriftRacingPage(BasePage):
    """Page Object для страницы /drift_racing2 (CarX Drift Racing 2)."""

    DOWNLOAD_BLOCK = (
        By.XPATH,
        "//*[contains(normalize-space(),'Скачать игру')]/ancestor::*"
        "[.//a[contains(@href,'play.google.com')] or "
        ".//a[contains(@href,'apps.apple.com')]][1]",
    )
    APP_STORE_LINK = (
        By.XPATH,
        "//a[contains(@href,'apps.apple.com')]",
    )
    GOOGLE_PLAY_LINK = (
        By.XPATH,
        "//a[contains(@href,'play.google.com')]",
    )

    def scroll_to_download_block(self) -> None:
        self.scroll_to_element(self.DOWNLOAD_BLOCK)

    def is_download_block_present(self) -> bool:
        return self.is_present(self.DOWNLOAD_BLOCK, timeout=10)

    def get_app_store_href(self) -> str | None:
        if not self.is_present(self.APP_STORE_LINK, timeout=5):
            return None
        return self.get_attribute(self.APP_STORE_LINK, "href")

    def get_google_play_href(self) -> str | None:
        if not self.is_present(self.GOOGLE_PLAY_LINK, timeout=5):
            return None
        return self.get_attribute(self.GOOGLE_PLAY_LINK, "href")

    def has_app_store_download(self) -> bool:
        href = self.get_app_store_href()
        return bool(href) and "apps.apple.com" in href

    def has_google_play_download(self) -> bool:
        href = self.get_google_play_href()
        return bool(href) and "play.google.com" in href
