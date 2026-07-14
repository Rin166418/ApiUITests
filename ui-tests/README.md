# UI-тесты для igrovoy.rt.ru

Автоматизированные UI-тесты для проверки функциональности сайта https://igrovoy.rt.ru/.

## Стек технологий

- **Python** 3.11+
- **Selenium** — для управления браузером
- **pytest** — тест-фреймворк
- **webdriver-manager** — автоматическое управление ChromeDriver
- **allure-pytest** — генерация красивых отчётов

## Архитектура

- **Page Object Model (POM)** — каждая страница представлена классом с локаторами и методами
- **BasePage** — базовый класс со всеми общими методами работы с элементами
- Локаторы — только XPath или CSS селекторы (никаких id/name напрямую в тестах)
- WebDriverWait с явными ожиданиями (без `time.sleep`)

## Установка зависимостей

```bash
python -m venv venv
source venv/bin/activate  # на macOS/Linux
# или на Windows: venv\Scripts\activate

pip install -r requirements.txt
```

## Структура проекта

```
project-root/
├── config/
│   └── config.py          # Конфигурация (BASE_URL, таймауты)
├── drivers/
│   └── driver_factory.py  # Фабрика для инициализации Chrome
├── pages/
│   ├── base_page.py       # Базовый класс для page objects
│   └── [page_objects]     # Page Object классы конкретных страниц
├── tests/
│   └── [test_*.py]        # Тесты
├── conftest.py            # Фикстуры и хуки pytest
├── pytest.ini             # Конфигурация pytest
├── requirements.txt       # Зависимости
├── .gitignore            # Исключения git
└── README.md             # Этот файл
```

## Запуск тестов

### Запустить все тесты
```bash
pytest
```

### Запустить тесты с отчётом Allure
```bash
pytest --alluredir=allure-results
```

### Запустить конкретный тест
```bash
pytest tests/test_example.py::test_name -v
```

### Запустить тесты с маркером
```bash
pytest -m smoke    # Запустить только smoke-тесты
pytest -m positive # Запустить позитивные тесты
```

### Запустить в headless-режиме
```bash
HEADLESS=true pytest
```

## Генерация Allure-отчётов

### Просмотреть отчёт локально
```bash
allure serve allure-results
```

### Сгенерировать HTML отчёт
```bash
allure generate allure-results -o allure-report
open allure-report/index.html  # на macOS
```

## Ветки в git

- **main** — конфигурация, инфраструктура, BasePage (без тестов и page objects)
- **py_a_test** — page object классы и все тесты

## Примечания

- Все локаторы должны быть вынесены в page object классы
- Все явные ожидания должны использовать WebDriverWait из BasePage
- При падении теста автоматически создаётся скриншот в папке `screenshots/`
- Скриншот также добавляется в Allure-отчёт
