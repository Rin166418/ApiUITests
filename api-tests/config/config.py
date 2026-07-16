import os

BASE_URL = os.getenv("EMPLOYEE_API_BASE_URL", "http://185.193.143.49:8080")
EMPLOYEES_ENDPOINT = "/api/employees"

DEFAULT_TIMEOUT = int(os.getenv("EMPLOYEE_API_TIMEOUT", "30"))
