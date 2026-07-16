import allure
import pytest

from utils.data_generator import generate_minimal_valid_employee, generate_valid_employee

@allure.epic("Employee Management API")
@allure.feature("CRUD сотрудника — позитивные сценарии")
class TestEmployeePositive:

    @allure.title("Создание сотрудника с полным набором валидных данных")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.positive
    def test_create_employee_full_data(self, api_client, created_employee_id):
        employee = generate_valid_employee()

        with allure.step("Создать сотрудника через POST /api/employees"):
            response = created_employee_id(employee.to_dict())

        with allure.step("Проверить статус-код 201"):
            assert response.status_code == 201, response.text

        with allure.step("Проверить структуру и значения ответа"):
            body = response.json()
            assert body["id"] is not None
            assert body["name"] == employee.name
            assert body["email"] == employee.email
            assert body["position"] == employee.position
            assert body["department"] == employee.department
            assert body["company"] == employee.company
            assert body["salary"] == pytest.approx(employee.salary)
            assert body.get("createdAt") is not None
            assert body.get("updatedAt") is not None

    @allure.title("Создание сотрудника с минимальным набором name и salary")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.positive
    def test_create_employee_minimal_data(self, api_client, created_employee_id):
        employee = generate_minimal_valid_employee()

        with allure.step("Создать сотрудника с минимальными полями name и salary"):
            response = created_employee_id(employee.to_dict())

        with allure.step("Проверить статус-код 201 и наличие имени"):
            assert response.status_code == 201, response.text
            body = response.json()
            assert body["name"] == employee.name
            assert body["salary"] == employee.salary
            assert body["id"] is not None

    @allure.title("Получение сотрудника по id после создания")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.positive
    def test_get_employee_by_id(self, api_client, created_employee_id):
        employee = generate_valid_employee()

        with allure.step("Создать сотрудника"):
            create_response = created_employee_id(employee.to_dict())
            employee_id = create_response.json()["id"]

        with allure.step("Получить сотрудника по id через GET"):
            get_response = api_client.get_employee(employee_id)

        with allure.step("Проверить статус-код 200 и совпадение данных"):
            assert get_response.status_code == 200
            body = get_response.json()
            assert body["id"] == employee_id
            assert body["name"] == employee.name
            assert body["email"] == employee.email

    @allure.title("Созданный сотрудник присутствует в общем списке")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.positive
    def test_created_employee_in_list(self, api_client, created_employee_id):
        employee = generate_valid_employee()

        with allure.step("Создать сотрудника"):
            create_response = created_employee_id(employee.to_dict())
            employee_id = create_response.json()["id"]

        with allure.step("Получить список всех сотрудников"):
            list_response = api_client.get_all_employees()

        with allure.step("Проверить, что созданный сотрудник есть в списке"):
            assert list_response.status_code == 200
            all_ids = [item["id"] for item in list_response.json()]
            assert employee_id in all_ids, f"id {employee_id} не найден в списке: {all_ids}"

    @allure.title("Полное обновление данных сотрудника через PUT")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.positive
    def test_update_employee_put(self, api_client, created_employee_id):
        employee = generate_valid_employee()

        with allure.step("Создать сотрудника"):
            create_response = created_employee_id(employee.to_dict())
            employee_id = create_response.json()["id"]

        updated_employee = generate_valid_employee()

        with allure.step("Полностью обновить данные сотрудника через PUT"):
            update_response = api_client.update_employee(employee_id, updated_employee.to_dict())

        with allure.step("Проверить, что данные обновились"):
            assert update_response.status_code == 200, update_response.text
            body = update_response.json()
            assert body["id"] == employee_id
            assert body["name"] == updated_employee.name
            assert body["email"] == updated_employee.email
            assert body["salary"] == pytest.approx(updated_employee.salary)

        with allure.step("Проверить через повторный GET, что изменения сохранились"):
            get_response = api_client.get_employee(employee_id)
            assert get_response.json()["name"] == updated_employee.name

    @allure.title("Частичное обновление данных сотрудника через PATCH")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.positive
    def test_update_employee_patch(self, api_client, created_employee_id):
        employee = generate_valid_employee()

        with allure.step("Создать сотрудника"):
            create_response = created_employee_id(employee.to_dict())
            employee_id = create_response.json()["id"]

        new_position = "Senior QA Automation Engineer"

        with allure.step("Частично обновить position, передав обязательное поле name"):
            patch_response = api_client.patch_employee(
                employee_id,
                {"name": employee.name, "position": new_position},
            )

        with allure.step("Проверить, что обновилось только указанное поле"):
            assert patch_response.status_code == 200, patch_response.text
            body = patch_response.json()
            assert body["position"] == new_position
            assert body["name"] == employee.name
            assert body["email"] == employee.email

    @allure.title("Удаление сотрудника")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.positive
    def test_delete_employee(self, api_client):
        employee = generate_valid_employee()

        with allure.step("Создать сотрудника для последующего удаления"):
            create_response = api_client.create_employee(employee.to_dict())
            employee_id = create_response.json()["id"]

        with allure.step("Удалить сотрудника через DELETE"):
            delete_response = api_client.delete_employee(employee_id)

        with allure.step("Проверить статус-код 204"):
            assert delete_response.status_code == 204

        with allure.step("Проверить, что повторный GET возвращает 404"):
            get_response = api_client.get_employee(employee_id)
            assert get_response.status_code == 404
