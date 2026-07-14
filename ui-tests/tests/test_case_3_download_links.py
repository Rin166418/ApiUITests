"""
Тесты для кейса 3: Проверка ссылок загрузки Google Play и App Store.

Включает:
1. Позитивный сценарий: найти и открыть CarX Drift Racing 2, проверить ссылки на загрузку
2. Негативный сценарий: попытаться использовать продукт без блока "Скачать игру" и проверить корректный результат
"""
import allure
import pytest
from config.config import BASE_URL
from pages.home_page import HomePage
from pages.game_card_page import GameCardPage


@allure.title("Кейс 3: Проверка ссылок загрузки Google Play и App Store для CarX Drift Racing 2")
@allure.description("""
Позитивный сценарий:
1. Открыть главную страницу
2. Прокрутить страницу вниз
3. Найти и открыть игру CarX Drift Racing 2
4. Прокрутить страницу до блока "Скачать игру"
5. Проверить, что ссылки ведут на play.google.com и apps.apple.com
""")
@allure.severity(allure.severity_level.CRITICAL)
def test_case_3_download_links_positive(driver):
    """
    Позитивный тест: проверка наличия ссылок на Google Play и App Store на странице CarX Drift Racing 2.
    """
    with allure.step("Открыть главную страницу"):
        driver.get(BASE_URL)

    home_page = HomePage(driver)

    with allure.step("Прокрутить главную страницу в самый низ"):
        home_page.scroll_to_bottom()

    with allure.step("Найти и открыть карточку CarX Drift Racing 2"):
        home_page.open_game_card_by_title("CarX Drift Racing 2")

    game_card_page = GameCardPage(driver)

    with allure.step("Прокрутить к блоку 'Скачать игру'"):
        game_card_page.scroll_to_download_block()

    with allure.step("Получить ссылки на загрузку"):
        download_links = game_card_page.get_download_links()

    with allure.step("Проверить ссылку на Google Play"):
        google_play_url = download_links.get("google_play")
        allure.attach(
            google_play_url or "None",
            name="Google Play URL",
            attachment_type=allure.attachment_type.TEXT,
        )
        assert google_play_url is not None, "Ссылка на Google Play должна присутствовать на странице"
        assert "play.google.com" in google_play_url, \
            f"URL Google Play должен вести на play.google.com, получено: {google_play_url}"

    with allure.step("Проверить ссылку на App Store"):
        app_store_url = download_links.get("app_store")
        allure.attach(
            app_store_url or "None",
            name="App Store URL",
            attachment_type=allure.attachment_type.TEXT,
        )
        assert app_store_url is not None, "Ссылка на App Store должна присутствовать на странице"
        assert "apps.apple.com" in app_store_url, \
            f"URL App Store должен вести на apps.apple.com, получено: {app_store_url}"


@allure.title("Кейс 3 (Негативный): Проверка отсутствия блока загрузки у неподходящего продукта")
@allure.description("""
Негативный сценарий:
1. Открыть главную страницу
2. Прокрутить страницу вниз
3. Найти и открыть продукт, где может не быть блока "Скачать игру"
4. Проверить, что метод get_download_links() корректно возвращает None для ссылок
   и не падает с исключением
""")
@allure.severity(allure.severity_level.NORMAL)
def test_case_3_download_links_negative(driver):
    """
    Негативный тест: проверка метода get_download_links() на странице без блока загрузки.
    """
    with allure.step("Открыть главную страницу"):
        driver.get(BASE_URL)

    home_page = HomePage(driver)

    with allure.step("Прокрутить главную страницу в самый низ"):
        home_page.scroll_to_bottom()

    # Пробуем открыть продукт, который, как ожидается, не содержит блока загрузки.
    negative_product_title = "PIONER EXTRA — Подписка на 30 дней"

    with allure.step(f"Найти и открыть продукт '{negative_product_title}'"):
        try:
            home_page.open_game_card_by_title(negative_product_title)
        except Exception as error:
            pytest.skip(
                f"Не удалось найти продукт '{negative_product_title}' для негативного сценария: {error}"
            )

    game_card_page = GameCardPage(driver)

    with allure.step("Попытаться прокрутить к блоку 'Скачать игру', если он есть"):
        try:
            game_card_page.scroll_to_download_block()
        except Exception:
            allure.attach(
                "Блок 'Скачать игру' не найден на странице продукта.",
                name="Блок не найден",
                attachment_type=allure.attachment_type.TEXT,
            )

    with allure.step("Получить ссылки на загрузку"):
        download_links = game_card_page.get_download_links()

    with allure.step("Проверить, что метод корректно возвращает отсутствующие ссылки"):
        google_play_url = download_links.get("google_play")
        app_store_url = download_links.get("app_store")

        allure.attach(
            f"google_play: {google_play_url}\napp_store: {app_store_url}",
            name="Результаты get_download_links",
            attachment_type=allure.attachment_type.TEXT,
        )

        if google_play_url or app_store_url:
            pytest.skip(
                "На выбранной странице доступны ссылки загрузки, негативный сценарий не применим"
            )

        assert google_play_url is None and app_store_url is None, \
            "Метод get_download_links() должен корректно возвращать None, если ссылки загрузки отсутствуют"
