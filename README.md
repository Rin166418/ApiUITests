# Автотесты Ростелеком

В репозитории находятся два проекта:

- `ui-tests` — UI-тесты сайта `https://igrovoy.rt.ru/`;
- `api-tests` — тесты сервиса управления сотрудниками.

Тесты написаны на Python с использованием `pytest` и Allure. UI-проект построен по Page Object Model и запускается в Google Chrome.

## Требования

Для запуска понадобятся:

- Python 3.9 или новее;
- Google Chrome;
- Allure Commandline;
- Docker Desktop для локального запуска API.

Проверить установку Allure:

```bash
allure --version
```

## UI-тесты

```bash
cd ui-tests
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python -m pytest --clean-alluredir --alluredir=allure-results
allure serve allure-results
```

Для запуска Chrome в headless-режиме:

```bash
HEADLESS=1 python -m pytest --clean-alluredir --alluredir=allure-results
```

Покрыты три основных сценария:

1. Поиск PIONER и проверка актуальной цены в карточке. (она стала стоить 699)
2. Поиск LEGO Batman без строки поиска и проверка минимальных системных требований.
3. Переход к CarX Drift Racing 2 и проверка ссылок Google Play и App Store.


## API-тесты

Удалённый стенд по умолчанию:

```text
http://185.193.143.49:8080
```

Если стенд доступен:

```bash
cd api-tests
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python -m pytest --clean-alluredir --alluredir=allure-results
allure serve allure-results
```

Если удалённый стенд недоступен, сервис можно запустить локально из репозитория:

```bash
git clone https://github.com/mxmrbkv/training_swagger.git
cd training_swagger
chmod +x gradlew
./gradlew build
docker compose up --build -d
```

Swagger после запуска доступен по адресу `http://localhost:8080/swagger-ui/index.html`.

На Mac с Apple Silicon в `Dockerfile` может потребоваться заменить образы `eclipse-temurin:17-jdk-alpine` и `eclipse-temurin:17-jre-alpine` на `eclipse-temurin:17-jdk` и `eclipse-temurin:17-jre`.

После запуска сервиса открыть новый терминал:

```bash
cd api-tests
source venv/bin/activate
EMPLOYEE_API_BASE_URL=http://localhost:8080 python -m pytest --clean-alluredir --alluredir=allure-results
allure serve allure-results
```

Остановить локальный сервис:

```bash
cd training_swagger
docker compose down
```

API-тесты покрывают позитивные и негативные сценарии для `GET`, `POST`, `PUT`, `PATCH` и `DELETE /api/employees`.

## Отдельные группы тестов

В обоих проектах доступны маркеры:

```bash
python -m pytest -m positive
python -m pytest -m negative
```

Параметр `--clean-alluredir` очищает результаты предыдущего запуска, поэтому в отчёте отображаются только актуальные тесты.

Чтобы сохранить статический Allure-отчёт:

```bash
allure generate allure-results -o allure-report --clean
allure open allure-report
```
