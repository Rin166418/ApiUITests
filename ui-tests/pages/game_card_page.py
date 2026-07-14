"""
GameCardPage — страница карточки/информации об игре
"""
import re
from pages.base_page import BasePage
from pages.game_card_page_locators import GameCardPageLocators


class GameCardPage(BasePage):
    """
    Page Object для страницы с информацией об игре.
    """
    
    def get_price(self) -> str:
        """
        Получает цену товара.
        
        :return: цена в виде строки (например, "699р")
        """
        price_text = self.get_text(GameCardPageLocators.PRICE)
        return price_text.strip()
    
    def get_min_requirements(self) -> dict:
        """
        Получает минимальные системные требования.
        
        :return: словарь с ключами: os, cpu, ram, gpu, storage
        """
        requirements = {
            "os": self._get_requirement_value(GameCardPageLocators.OS_REQUIREMENT),
            "cpu": self._get_requirement_value(GameCardPageLocators.CPU_REQUIREMENT),
            "ram": self._get_requirement_value(GameCardPageLocators.RAM_REQUIREMENT),
            "gpu": self._get_requirement_value(GameCardPageLocators.GPU_REQUIREMENT),
            "storage": self._get_requirement_value(GameCardPageLocators.STORAGE_REQUIREMENT),
        }
        return requirements
    
    def _get_requirement_value(self, locator: tuple) -> str:
        """
        Вспомогательный метод для получения значения требования.
        
        :param locator: локатор требования
        :return: значение требования
        """
        try:
            return self.get_text(locator).strip()
        except:
            return "Not specified"
    
    def scroll_to_download_block(self):
        """
        Скроллит страницу к блоку "Скачать игру".
        """
        self.scroll_to_element(GameCardPageLocators.DOWNLOAD_BLOCK)
    
    def get_download_links(self) -> dict:
        """
        Получает ссылки для скачивания (Google Play и App Store).
        
        :return: словарь с ключами 'google_play' и 'app_store'
                 значения: URL ссылки или None если нет
        """
        download_links = {
            "google_play": None,
            "app_store": None,
        }
        
        # Проверяем наличие ссылки на Google Play
        if self.is_element_visible(GameCardPageLocators.GOOGLE_PLAY_LINK):
            download_links["google_play"] = self.find_element(GameCardPageLocators.GOOGLE_PLAY_LINK).get_attribute("href")
        
        # Проверяем наличие ссылки на App Store
        if self.is_element_visible(GameCardPageLocators.APP_STORE_LINK):
            download_links["app_store"] = self.find_element(GameCardPageLocators.APP_STORE_LINK).get_attribute("href")
        
        return download_links
