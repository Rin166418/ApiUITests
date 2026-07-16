from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Employee:
    """Данные сотрудника для API-запросов."""

    name: str
    email: str | None = None
    position: str | None = None
    department: str | None = None
    company: str | None = None
    salary: float | None = None

    def to_dict(self) -> dict:
        return {k: v for k, v in self.__dict__.items() if v is not None}
