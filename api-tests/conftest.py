import allure
import pytest

from clients.employee_client import EmployeeClient


@pytest.fixture(scope="session")
def api_client() -> EmployeeClient:
    return EmployeeClient()


@pytest.fixture
def created_employee_id(api_client):
    """Создаёт сотрудников и удаляет их после теста."""
    created_ids = []

    def _create(employee_data: dict):
        response = api_client.create_employee(employee_data)
        if response.status_code == 201:
            employee_id = response.json().get("id")
            if employee_id is not None:
                created_ids.append(employee_id)
        return response

    yield _create

    for employee_id in created_ids:
        with allure.step(f"Teardown: удалить сотрудника id={employee_id}, если он ещё существует"):
            api_client.delete_employee(employee_id)
