import allure
import pytest

from pages.catalog_page import CatalogPage
from pages.game_card_page import GameCardPage
from pages.home_page import HomePage

GAME_TITLE = "LEGO Batman: Legacy of the Dark Knight"

EXPECTED_MIN_REQUIREMENTS = {
    "os": "Windows 11",
    "cpu": "Intel CPU Core i5-9600K",
    "ram": "16 Гб",
    "gpu": "NVIDIA GeForce RTX 2070",
    "storage": "50 ГБ",
}


@allure.epic("igrovoy.rt.ru")
@allure.feature("Каталог PC — минимальные системные требования")
class TestMinRequirements:

    @allure.title("Позитивный: минимальные требования LEGO Batman соответствуют эталону")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.positive
    def test_lego_batman_min_requirements(self, driver):
        home_page = HomePage(driver)
        catalog_page = CatalogPage(driver)
        game_card_page = GameCardPage(driver)

        with allure.step("Открыть главную страницу"):
            home_page.open_home()

        with allure.step("Навести курсор на 'Игры' и перейти в 'PC'"):
            home_page.go_to_games_pc_catalog()

        with allure.step(f"Найти в списке (без поиска) игру '{GAME_TITLE}'"):
            card_link = catalog_page.find_game_card_by_title(GAME_TITLE)
            assert card_link is not None, (
                f"Игра '{GAME_TITLE}' не найдена в каталоге при прокрутке"
            )

        with allure.step("Открыть карточку найденной игры"):
            card_link.click()

        with allure.step("Получить минимальные системные требования из карточки"):
            actual_requirements = game_card_page.get_min_requirements()

        for field, expected_value in EXPECTED_MIN_REQUIREMENTS.items():
            with allure.step(
                f"Проверить поле '{field}': ожидается '{expected_value}'"
            ):
                actual_value = actual_requirements.get(field)
                assert actual_value == expected_value, (
                    f"Поле '{field}': ожидалось '{expected_value}', "
                    f"фактически '{actual_value}'. Все требования: {actual_requirements}"
                )

    @allure.title("Негативный: поиск несуществующей игры в списке без использования поиска")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.negative
    def test_nonexistent_game_not_found_in_catalog(self, driver):
        home_page = HomePage(driver)
        catalog_page = CatalogPage(driver)

        with allure.step("Открыть главную страницу"):
            home_page.open_home()

        with allure.step("Навести курсор на 'Игры' и перейти в 'PC'"):
            home_page.go_to_games_pc_catalog()

        with allure.step("Попытаться найти несуществующую игру без использования поиска"):
            card_link = catalog_page.find_game_card_by_title(
                "NonExistentGame12345XYZ", max_scrolls=15
            )

        with allure.step("Проверить, что метод корректно вернул None"):
            assert card_link is None, (
                "Ожидалось, что несуществующая игра не будет найдена (None), "
                f"но метод вернул элемент: {card_link}"
            )
