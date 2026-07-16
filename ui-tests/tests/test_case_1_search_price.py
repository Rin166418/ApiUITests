import allure
import pytest

from pages.catalog_page import CatalogPage
from pages.game_card_page import GameCardPage
from pages.home_page import HomePage

# В задании указана цена 699р, но сейчас PIONER стоит 999р.
# Если цена на сайте изменится, нужно обновить значение константы.
EXPECTED_PIONER_PRICE_RUB = 999


@allure.epic("igrovoy.rt.ru")
@allure.feature("Каталог PC: поиск")
class TestSearchAndPrice:

    @allure.title("Позитивный: поиск игры Pioner и проверка цены в карточке")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.positive
    def test_search_pioner_and_check_price(self, driver):
        home_page = HomePage(driver)
        catalog_page = CatalogPage(driver)
        game_card_page = GameCardPage(driver)

        with allure.step("Открыть главную страницу"):
            home_page.open_home()

        with allure.step("Навести курсор на 'Игры' и перейти в 'PC'"):
            home_page.go_to_games_pc_catalog()

        with allure.step("Ввести в поиске 'Pioner'"):
            home_page.search_in_header("Pioner")
            catalog_page.wait_for_search_results("Pioner")

        with allure.step("Открыть первую карточку из результатов поиска"):
            catalog_page.open_first_result()

        with allure.step("Проверить цену внутри карточки товара"):
            actual_price_rub = game_card_page.get_price_rub()
            assert actual_price_rub == EXPECTED_PIONER_PRICE_RUB, (
                f"Ожидалась цена {EXPECTED_PIONER_PRICE_RUB} ₽, "
                f"фактическая цена в карточке: {actual_price_rub} ₽ "
                f"(текст: '{game_card_page.get_price()}')"
            )

    @allure.title("Негативный: поиск по несуществующей игре")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.negative
    def test_search_nonexistent_game(self, driver):
        home_page = HomePage(driver)
        catalog_page = CatalogPage(driver)

        with allure.step("Открыть главную страницу"):
            home_page.open_home()

        with allure.step("Навести курсор на 'Игры' и перейти в 'PC'"):
            home_page.go_to_games_pc_catalog()

        with allure.step("Ввести в поиске заведомо несуществующий запрос"):
            query = "asdkjhaskjdh12345nonexistentgame"
            home_page.search_in_header(query)
            catalog_page.wait_for_search_results(query)

        with allure.step("Проверить, что результатов поиска нет"):
            results_count = catalog_page.get_results_count()
            assert catalog_page.has_no_results_message() or results_count == 0, (
                f"Ожидалось 0 результатов по несуществующему запросу, "
                f"фактически найдено: {results_count}"
            )
