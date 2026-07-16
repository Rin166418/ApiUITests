import allure
import pytest

from pages.drift_racing_page import DriftRacingPage
from pages.home_page import HomePage


@allure.epic("igrovoy.rt.ru")
@allure.feature("Страница игры — блок 'Скачать игру'")
class TestDownloadLinks:

    @allure.title("Позитивный: на странице CarX Drift Racing 2 доступны ссылки Google Play и App Store")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.positive
    def test_carx_drift_racing_download_links(self, driver):
        home_page = HomePage(driver)
        drift_racing_page = DriftRacingPage(driver)

        with allure.step("Открыть главную страницу"):
            home_page.open_home()

        with allure.step("Прокрутить страницу в самый низ и открыть CarX Drift Racing 2"):
            home_page.open_carx_drift_racing_2()

        with allure.step("Найти блок 'Скачать игру'"):
            assert drift_racing_page.is_download_block_present(), (
                "Блок 'Скачать игру' не найден на странице"
            )
            drift_racing_page.scroll_to_download_block()

        with allure.step("Проверить наличие корректной ссылки на Google Play"):
            google_play_href = drift_racing_page.get_google_play_href()
            assert drift_racing_page.has_google_play_download(), (
                f"Ссылка на Google Play отсутствует или некорректна: {google_play_href}"
            )

        with allure.step("Проверить наличие корректной ссылки на App Store"):
            app_store_href = drift_racing_page.get_app_store_href()
            assert drift_racing_page.has_app_store_download(), (
                f"Ссылка на App Store отсутствует или некорректна: {app_store_href}"
            )
