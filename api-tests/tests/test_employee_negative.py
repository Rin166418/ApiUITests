import allure
import pytest

from utils.data_generator import (
    generate_employee_with_blank_name,
    generate_employee_with_negative_salary,
    generate_employee_with_too_long_email,
    generate_employee_with_too_long_name,
    generate_employee_with_wrong_salary_type,
    generate_employee_with_zero_salary,
    generate_employee_without_name,
    generate_valid_employee,
)

NON_EXISTENT_ID = 999999999


@allure.epic("Employee Management API")
@allure.feature("CRUD сотрудника: негативные сценарии")
class TestEmployeeNegative:

    @allure.title("Создание сотрудника без обязательного поля name")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.negative
    def test_create_employee_without_name(self, api_client):
        with allure.step("Отправить POST без поля name"):
            response = api_client.create_employee(generate_employee_without_name())

        with allure.step("Проверить статус-код 400"):
            assert response.status_code == 400, response.text

    @allure.title("Создание сотрудника с пустым name")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.negative
    def test_create_employee_with_blank_name(self, api_client):
        with allure.step("Отправить POST с пустой строкой в name"):
            response = api_client.create_employee(generate_employee_with_blank_name())

        with allure.step("Проверить статус-код 400"):
            assert response.status_code == 400, response.text

    @allure.title("Создание сотрудника с name длиннее 100 символов")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.negative
    def test_create_employee_with_too_long_name(self, api_client):
        with allure.step("Отправить POST с name длиной 101 символ"):
            response = api_client.create_employee(generate_employee_with_too_long_name())

        with allure.step("Проверить статус-код 400"):
            assert response.status_code == 400, response.text

    @allure.title("Создание сотрудника с отрицательной зарплатой")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.negative
    def test_create_employee_with_negative_salary(self, api_client):
        with allure.step("Отправить POST с отрицательным salary"):
            response = api_client.create_employee(generate_employee_with_negative_salary())

        with allure.step("Проверить статус-код 400"):
            assert response.status_code == 400, response.text

    @allure.title("Создание сотрудника с нулевой зарплатой (exclusiveMinimum=0)")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.negative
    def test_create_employee_with_zero_salary(self, api_client):
        with allure.step("Отправить POST с salary=0"):
            response = api_client.create_employee(generate_employee_with_zero_salary())

        with allure.step("Проверить статус-код 400"):
            assert response.status_code == 400, response.text

    @allure.title("Создание сотрудника со строкой вместо числа в salary")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.negative
    def test_create_employee_with_wrong_salary_type(self, api_client):
        with allure.step("Отправить POST со строковым значением salary"):
            response = api_client.create_employee(generate_employee_with_wrong_salary_type())

        with allure.step("Проверить, что сервис отклонил некорректный тип salary"):
            assert response.status_code in (400, 500), response.text

    @allure.title("Создание сотрудника с email длиннее 100 символов")
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.negative
    def test_create_employee_with_too_long_email(self, api_client):
        with allure.step("Отправить POST с email длиной больше 100 символов"):
            response = api_client.create_employee(generate_employee_with_too_long_email())

        with allure.step("Проверить статус-код 400"):
            assert response.status_code == 400, response.text

    @allure.title("Получение несуществующего сотрудника по id")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.negative
    def test_get_nonexistent_employee(self, api_client):
        with allure.step(f"Отправить GET для несуществующего id={NON_EXISTENT_ID}"):
            response = api_client.get_employee(NON_EXISTENT_ID)

        with allure.step("Проверить статус-код 404"):
            assert response.status_code == 404, response.text

    @allure.title("Обновление (PUT) несуществующего сотрудника")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.negative
    def test_update_nonexistent_employee(self, api_client):
        employee = generate_valid_employee()

        with allure.step(f"Отправить PUT для несуществующего id={NON_EXISTENT_ID}"):
            response = api_client.update_employee(NON_EXISTENT_ID, employee.to_dict())

        with allure.step("Проверить статус-код 404"):
            assert response.status_code == 404, response.text

    @allure.title("Частичное обновление (PATCH) несуществующего сотрудника")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.negative
    def test_patch_nonexistent_employee(self, api_client):
        with allure.step(f"Отправить PATCH для несуществующего id={NON_EXISTENT_ID}"):
            response = api_client.patch_employee(
                NON_EXISTENT_ID,
                {"name": "Несуществующий сотрудник", "position": "QA"},
            )

        with allure.step("Проверить статус-код 404"):
            assert response.status_code == 404, response.text

    @allure.title("Удаление несуществующего сотрудника")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.negative
    def test_delete_nonexistent_employee(self, api_client):
        with allure.step(f"Отправить DELETE для несуществующего id={NON_EXISTENT_ID}"):
            response = api_client.delete_employee(NON_EXISTENT_ID)

        with allure.step("Проверить статус-код 404"):
            assert response.status_code == 404, response.text

    @allure.title("Повторное удаление уже удалённого сотрудника")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.negative
    def test_delete_employee_twice(self, api_client):
        employee = generate_valid_employee()

        with allure.step("Создать сотрудника"):
            create_response = api_client.create_employee(employee.to_dict())
            employee_id = create_response.json()["id"]

        with allure.step("Удалить сотрудника первый раз"):
            first_delete = api_client.delete_employee(employee_id)
            assert first_delete.status_code == 204

        with allure.step("Повторно удалить того же сотрудника"):
            second_delete = api_client.delete_employee(employee_id)

        with allure.step("Проверить статус-код 404 при повторном удалении"):
            assert second_delete.status_code == 404, second_delete.text

    @allure.title("Получение сотрудника по некорректному (нечисловому) id")
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.negative
    def test_get_employee_with_invalid_id_format(self, api_client):
        with allure.step("Отправить GET с нечисловым id в пути"):
            response = api_client.get_employee("not-a-valid-id")

        with allure.step("Проверить, что запрос не завершился успехом (не 200)"):
            assert response.status_code != 200, (
                f"Ожидалась ошибка при нечисловом id, но получен статус "
                f"{response.status_code}: {response.text}"
            )
