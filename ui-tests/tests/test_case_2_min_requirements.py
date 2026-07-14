"""
Тесты для кейса 2: Проверка минимальных системных требований игры.

Включает:
1. Позитивный сценарий: поиск LEGO Batman, проверка требований
2. Негативный сценарий: поиск несуществующей игры с корректной обработкой ошибки
"""
import allure
import pytest
from config.config import BASE_URL
from pages.home_page import HomePage
from pages.catalog_page import CatalogPage, GameNotFoundError
from pages.game_card_page import GameCardPage


@allure.title("Кейс 2: Проверка минимальных требований LEGO Batman")
@allure.description("""
Позитивный сценарий:
1. Навести курсор на "Игры" в верхнем меню
2. Нажать "PC" для переходу в каталог PC-игр
3. Найти в списке игру "LEGO Batman: Legacy of the Dark Knight" без использования поиска
4. Открыть карточку игры
5. Проверить минимальные системные требования:
   - ОС: Windows 11
   - Процессор: Intel CPU Core i5-9600K
   - ОЗУ: 16 Гб
   - Видеокарта: NVIDIA GeForce RTX 2070
   - Жёсткий диск: 50 ГБ
""")
@allure.severity(allure.severity_level.CRITICAL)
def test_case_2_min_requirements_positive(driver):
    """
    Позитивный тест: поиск LEGO Batman и проверка минимальных требований.
    
    Шаги:
    1. Переходим на главную страницу
    2. Наводим курсор на меню "Игры"
    3. Кликаем на "PC" для фильтрации
    4. Ищем "LEGO Batman: Legacy of the Dark Knight" прокруткой списка
    5. Открываем карточку
    6. Получаем требования и проверяем каждое поле
    """
    # Эталонные требования для сравнения
    expected_requirements = {
        "os": "Windows 11",
        "cpu": "Intel CPU Core i5-9600K",
        "ram": "16 Гб",
        "gpu": "NVIDIA GeForce RTX 2070",
        "storage": "50 ГБ",
    }
    
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
    
    # Шаг 4: Поиск игры по названию в списке (без использования поиска)
    with allure.step("Поиск игры 'LEGO Batman: Legacy of the Dark Knight' в списке"):
        game_card = catalog_page.find_game_card_by_title("LEGO Batman: Legacy of the Dark Knight")
    
    # Шаг 5: Открытие карточки
    with allure.step("Открытие карточки игры"):
        game_card.click()
    
    game_card_page = GameCardPage(driver)
    
    # Шаг 6: Получение требований
    with allure.step("Получение минимальных системных требований"):
        actual_requirements = game_card_page.get_min_requirements()
    
    # Шаг 7: Проверка каждого требования
    with allure.step("Проверка OS (Операционная система)"):
        allure.attach(
            f"Ожидается: {expected_requirements['os']}\nПолучено: {actual_requirements['os']}",
            name="Сравнение ОС",
            attachment_type=allure.attachment_type.TEXT
        )
        assert expected_requirements["os"] in actual_requirements["os"], \
            f"ОС не совпадает. Ожидается '{expected_requirements['os']}', получено '{actual_requirements['os']}'"
    
    with allure.step("Проверка CPU (Процессор)"):
        allure.attach(
            f"Ожидается: {expected_requirements['cpu']}\nПолучено: {actual_requirements['cpu']}",
            name="Сравнение Процессора",
            attachment_type=allure.attachment_type.TEXT
        )
        assert expected_requirements["cpu"] in actual_requirements["cpu"], \
            f"Процессор не совпадает. Ожидается '{expected_requirements['cpu']}', получено '{actual_requirements['cpu']}'"
    
    with allure.step("Проверка RAM (Оперативная память)"):
        allure.attach(
            f"Ожидается: {expected_requirements['ram']}\nПолучено: {actual_requirements['ram']}",
            name="Сравнение ОЗУ",
            attachment_type=allure.attachment_type.TEXT
        )
        assert expected_requirements["ram"] in actual_requirements["ram"], \
            f"ОЗУ не совпадает. Ожидается '{expected_requirements['ram']}', получено '{actual_requirements['ram']}'"
    
    with allure.step("Проверка GPU (Видеокарта)"):
        allure.attach(
            f"Ожидается: {expected_requirements['gpu']}\nПолучено: {actual_requirements['gpu']}",
            name="Сравнение Видеокарты",
            attachment_type=allure.attachment_type.TEXT
        )
        assert expected_requirements["gpu"] in actual_requirements["gpu"], \
            f"Видеокарта не совпадает. Ожидается '{expected_requirements['gpu']}', получено '{actual_requirements['gpu']}'"
    
    with allure.step("Проверка Storage (Жёсткий диск)"):
        allure.attach(
            f"Ожидается: {expected_requirements['storage']}\nПолучено: {actual_requirements['storage']}",
            name="Сравнение Жёсткого диска",
            attachment_type=allure.attachment_type.TEXT
        )
        assert expected_requirements["storage"] in actual_requirements["storage"], \
            f"Жёсткий диск не совпадает. Ожидается '{expected_requirements['storage']}', получено '{actual_requirements['storage']}'"


@allure.title("Кейс 2 (Негативный): Поиск несуществующей игры в списке")
@allure.description("""
Негативный сценарий:
1. Навести курсор на "Игры" в верхнем меню
2. Нажать "PC" для переходу в каталог PC-игр
3. Попытаться найти несуществующую игру "NonExistentGame12345" в списке
4. Проверить, что метод выбрасывает понятное исключение GameNotFoundError
   (а не сырое Selenium исключение)
""")
@allure.severity(allure.severity_level.NORMAL)
def test_case_2_nonexistent_game_negative(driver):
    """
    Негативный тест: поиск несуществующей игры в списке.
    
    Проверяет, что метод find_game_card_by_title() корректно обрабатывает
    ситуацию, когда игра не найдена, и выбрасывает понятное исключение.
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
    
    # Шаг 4: Попытка найти несуществующую игру
    with allure.step("Попытка найти несуществующую игру 'NonExistentGame12345'"):
        with pytest.raises(GameNotFoundError) as exc_info:
            catalog_page.find_game_card_by_title("NonExistentGame12345")
        
        # Проверяем, что сообщение об ошибке понятное и информативное
        error_message = str(exc_info.value)
        
        allure.attach(
            f"Полученное исключение: {error_message}",
            name="Сообщение об ошибке",
            attachment_type=allure.attachment_type.TEXT
        )
        
        # Проверяем, что исключение содержит названием игры и информацию о попытках
        assert "NonExistentGame12345" in error_message, \
            f"Сообщение об ошибке должно содержать название игры"
        assert "не найдена" in error_message, \
            f"Сообщение об ошибке должно содержать информацию об отсутствии игры"
