from faker import Faker

from models.employee import Employee

fake = Faker("ru_RU")


def generate_valid_employee(**overrides) -> Employee:
    """Генерирует валидного сотрудника согласно EmployeeRequestDTO."""
    data = {
        "name": fake.name()[:100],
        "email": fake.email()[:100],
        "position": fake.job()[:100],
        "department": fake.word()[:100],
        "company": fake.company()[:100],
        "salary": round(fake.pyfloat(min_value=10000, max_value=500000, right_digits=2), 2),
    }
    data.update(overrides)
    return Employee(**data)


def generate_minimal_valid_employee(**overrides) -> Employee:
    """Минимальные данные, принимаемые текущей реализацией API."""
    data = {"name": fake.name()[:100], "salary": 1.0}
    data.update(overrides)
    return Employee(**data)


def generate_employee_without_name() -> dict:
    """Невалидные данные: отсутствует обязательное поле name."""
    return {
        "email": fake.email(),
        "position": fake.job(),
        "salary": 50000.0,
    }


def generate_employee_with_blank_name() -> dict:
    """Невалидные данные: name — пустая строка (minLength=1)."""
    return {"name": "", "email": fake.email(), "salary": 50000.0}


def generate_employee_with_too_long_name() -> dict:
    """Невалидные данные: name длиннее maxLength=100."""
    return {"name": "A" * 101, "salary": 50000.0}


def generate_employee_with_negative_salary() -> dict:
    """Невалидные данные: salary <= 0 (exclusiveMinimum=0)."""
    return {"name": fake.name(), "salary": -100.0}


def generate_employee_with_zero_salary() -> dict:
    """Невалидные данные: salary == 0, что запрещено exclusiveMinimum."""
    return {"name": fake.name(), "salary": 0}


def generate_employee_with_wrong_salary_type() -> dict:
    """Невалидные данные: salary передан строкой вместо числа."""
    return {"name": fake.name(), "salary": "not-a-number"}


def generate_employee_with_too_long_email() -> dict:
    """Невалидные данные: email длиннее maxLength=100."""
    return {"name": fake.name(), "email": ("a" * 95) + "@a.com"}
