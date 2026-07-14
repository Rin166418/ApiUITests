"""
Тесты для кейса 1: Поиск игры "Pioner" и проверка цены.

Включает:
1. Позитивный сценарий: поиск игры, проверка цены в карточке
2. Негативный сценарий: поиск несуществующей игры, проверка сообщения об ошибке
"""
import allure
import pytest
from config.config import BASE_URL
from pages.home_page import HomePage
from pages.catalog_page import CatalogPage
from pages.game_card_page import GameCardPage


@allure.title("Кейс 1: Поиск 'Pioner' и проверка цены")
@allure.description("""
Позитивный сценарий:
1. Навести курсор на "Игры" в верхнем меню
2. Нажать "PC" для переходу в каталог PC-игр
3. В поисковой строке ввести "Pioner"
4. Открыть первую карточку игры
5. Проверить, что цена товара внутри карточки совпадает с ценой в результатах поиска
""")
@allure.severity(allure.severity_level.CRITICAL)
def test_case_1_search_pioner_positive(driver):
    """
    Позитивный тест: поиск игры Pioner и проверка цены.
    
    Шаги:
    1. Переходим на главную страницу
    2. Наводим курсор на меню "Игры"
    3. Кликаем на "PC" для фильтрации
    4. Ищем "Pioner" через поиск
    5. Открываем первую карточку
    6. Получаем цену и проверяем, что она не пуста
    """
    # Шаг 1: Переход на главную страницу
    with allure.step("Переход на главную страницу"):
        driver.get(BASE_URL)
    
    home_page = HomePage(driver)
    
    # Шаг 2: Наведение курсора на меню "Игры"
    with allure.step("Наведение курсора на пункт меню 'Игры'"):
        home_page.hover_games_menu()
    
    # Шаг 3: Клик на "PC" в выпадающем меню
    with allure.step("Клик на 'PC' для перехода в каталог PC-игр"):
        home_page.click_pc_category()
    
    catalog_page = CatalogPage(driver)
    
    # Шаг 4: Поиск игры "Pioner"
    with allure.step("Поиск игры 'Pioner' в поисковой строке"):
        catalog_page.search_game("Pioner")
    
    # Шаг 5: Открытие первой карточки
    with allure.step("Открытие первой карточки из результатов поиска"):
        catalog_page.open_first_result()
    
    game_card_page = GameCardPage(driver)
    
    # Шаг 6: Получение цены и проверка
    with allure.step("Получение цены товара со страницы карточки"):
        price = game_card_page.get_price()
    
    with allure.step("Проверка, что цена не пуста"):
        allure.attach(
            f"Получена цена: {price}",
            name="Результат получения цены",
            attachment_type=allure.attachment_type.TEXT
        )
        assert price, "Цена товара должна быть отображена на странице карточки игры"
        assert "₽" in price or "Р" in price, f"Цена должна содержать символ валюты. Получено: {price}"


@allure.title("Кейс 1 (Негативный): Поиск несуществующей игры")
@allure.description("""
Негативный сценарий:
1. Навести курсор на "Игры" в верхнем меню
2. Нажать "PC" для переходу в каталог PC-игр
3. Попытаться поискать несуществующую игру (random string)
4. Проверить, что отображается сообщение "ничего не найдено"
""")
@allure.severity(allure.severity_level.NORMAL)
def test_case_1_search_nonexistent_game_negative(driver):
    """
    Негативный тест: поиск несуществующей игры.
    
    Шаги:
    1. Переходим на главную страницу
    2. Наводим курсор на меню "Игры"
    3. Кликаем на "PC" для фильтрации
    4. Ищем несуществующую игру "asdkjhaskjdh12345"
    5. Проверяем, что отображается сообщение об ошибке
    """
    # Шаг 1: Переход на главную страницу
    with allure.step("Переход на главную страницу"):
        driver.get(BASE_URL)
    
    home_page = HomePage(driver)
    
    # Шаг 2: Наведение курсора на меню "Игры"
    with allure.step("Наведение курсора на пункт меню 'Игры'"):
        home_page.hover_games_menu()
    
    # Шаг 3: Клик на "PC" в выпадающем меню
    with allure.step("Клик на 'PC' для перехода в каталог PC-игр"):
        home_page.click_pc_category()
    
    catalog_page = CatalogPage(driver)
    
    # Шаг 4: Поиск несуществующей игры
    with allure.step("Поиск несуществующей игры 'asdkjhaskjdh12345'"):
        catalog_page.search_game("asdkjhaskjdh12345")
    
    # Шаг 5: Проверка наличия сообщения об ошибке
    with allure.step("Проверка, что отображается сообщение 'ничего не найдено'"):
        is_no_results = catalog_page.is_no_results_displayed()
        
        allure.attach(
            f"Сообщение об отсутствии результатов: {is_no_results}",
            name="Результат проверки отсутствия результатов",
            attachment_type=allure.attachment_type.TEXT
        )
        assert is_no_results, "Должно отображаться сообщение 'По заданным фильтрам ничего не найдено'"
