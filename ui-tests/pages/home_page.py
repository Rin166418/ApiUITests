from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage


class HomePage(BasePage):
    """Page Object для главной страницы igrovoy.rt.ru"""

    GAMES_MENU_ITEM = (
        By.XPATH,
        "//a[contains(@class,'menuItem') and normalize-space(text())='Игры']",
    )
    PC_SUBMENU_LINK = (
        By.XPATH,
        "//a[normalize-space()='PC' and "
        "(contains(@href,'/catalog/game-pc') or contains(@href,'/games/pc'))]",
    )
    SEARCH_INPUT = (
        By.XPATH,
        "//input[@placeholder='Поиск' or contains(@class,'TextFieldInput')]",
    )
    SUBSCRIPTIONS_MENU_ITEM = (
        By.XPATH,
        "//a[contains(normalize-space(),'Подписки')]",
    )
    CARX_DRIFT_RACING_LINK = (
        By.XPATH,
        "//a[contains(normalize-space(),'CarX Drift Racing 2')]",
    )

    def open_home(self) -> None:
        self.open("/")

    def go_to_games_pc_catalog(self) -> None:
        self.hover(self.GAMES_MENU_ITEM)
        self.click(self.PC_SUBMENU_LINK)

    def search_in_header(self, query: str) -> None:
        """Ввести запрос в поисковую строку шапки и отправить поиск (Enter)."""
        search_input = self.find_visible(self.SEARCH_INPUT)
        search_input.clear()
        search_input.send_keys(query)
        search_input.send_keys(Keys.ENTER)

    def open_carx_drift_racing_2(self) -> None:
        """Открыть CarX Drift Racing 2 из выпадающего меню «Подписки»."""
        self.hover(self.SUBSCRIPTIONS_MENU_ITEM)
        self.click(self.CARX_DRIFT_RACING_LINK)
