# Employee Management API

API-тесты сервиса управления сотрудниками на Requests, pytest и Allure.

## Сервис

- Удалённый: `http://185.193.143.49:8080`
- Локально (при недоступности удалённого): поднять через Docker из
  https://github.com/mxmrbkv/training_swagger, затем передать URL через
  переменную окружения `EMPLOYEE_API_BASE_URL` (по умолчанию используется
  удалённый адрес).

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

Против локального сервиса:

```bash
EMPLOYEE_API_BASE_URL=http://localhost:8080 python -m pytest --clean-alluredir --alluredir=allure-results
```

Команды запуска локального сервиса приведены в общем `README.md` в корне репозитория.

Только позитивные/негативные:

```bash
python -m pytest -m positive
python -m pytest -m negative
```

## Просмотр Allure-отчёта

```bash
allure serve allure-results
```

Сохранить HTML-отчёт:

```bash
allure generate allure-results -o allure-report --clean
allure open allure-report
```

В Allure для каждого запроса сохраняются метод, URL, тело запроса, статус, заголовки и тело ответа.

## Структура

```
config/     - базовый URL и таймауты
clients/    - клиенты для отправки запросов
models/     - модель Employee
utils/      - генератор тестовых данных
tests/      - позитивные и негативные тесты
conftest.py - фикстуры и удаление созданных сотрудников после теста
```

## Покрытые эндпоинты (по OpenAPI-спецификации сервиса)

| Метод  | Путь                     | Позитив | Негатив                                  |
|--------|--------------------------|---------|-------------------------------------------|
| GET    | /api/employees           | ✅      | нет                                        |
| POST   | /api/employees           | ✅      | без name, пустой name, name>100, salary<=0, salary не число, email>100 |
| GET    | /api/employees/{id}      | ✅      | несуществующий id, нечисловой id           |
| PUT    | /api/employees/{id}      | ✅      | несуществующий id                          |
| PATCH  | /api/employees/{id}      | ✅      | несуществующий id                          |
| DELETE | /api/employees/{id}      | ✅      | несуществующий id, повторное удаление      |
