# UI-тесты igrovoy.rt.ru

Проект содержит UI-тесты на Selenium, pytest и Allure. Для организации кода используется Page Object Model.

## Установка

```bash
python3 -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Запуск тестов

```bash
python -m pytest --clean-alluredir --alluredir=allure-results
```

Headless-режим:

```bash
HEADLESS=1 python -m pytest --clean-alluredir --alluredir=allure-results
```

Только позитивные/негативные:

```bash
python -m pytest -m positive
python -m pytest -m negative
```

## Просмотр Allure-отчёта

```bash
allure serve allure-results
# или
allure generate allure-results -o allure-report --clean
allure open allure-report
```

Для быстрого просмотра без сохранения отчёта:

```bash
allure serve allure-results
```

## Структура проекта

```
config/          - адрес сайта и таймауты
drivers/         - настройка Chrome WebDriver
pages/           - классы Page Object
tests/           - тестовые сценарии
conftest.py      - фикстура браузера и скриншоты при падении
```

## Тестовые сценарии

1. Поиск PIONER и проверка цены внутри карточки.
2. Поиск LEGO Batman в каталоге без строки поиска и проверка системных требований.
3. Проверка ссылок Google Play и App Store для CarX Drift Racing 2.

Цена PIONER на сайте может меняться. Ожидаемое значение хранится в константе `EXPECTED_PIONER_PRICE_RUB` в `tests/test_case_1_search_price.py`.

Перед новым запуском используется `--clean-alluredir`, чтобы старые результаты не попадали в отчёт.
