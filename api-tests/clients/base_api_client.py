from __future__ import annotations
import json

import allure
import requests

from config.config import BASE_URL, DEFAULT_TIMEOUT


class BaseApiClient:
    """Выполняет HTTP-запросы и добавляет данные в Allure."""

    def __init__(self, base_url: str = BASE_URL):
        self.base_url = base_url
        self.session = requests.Session()

    def _full_url(self, path: str) -> str:
        return f"{self.base_url}{path}"

    def _attach_to_allure(self, method: str, url: str, request_body, response: requests.Response) -> None:
        request_info = {
            "method": method,
            "url": url,
            "body": request_body,
        }
        allure.attach(
            json.dumps(request_info, ensure_ascii=False, indent=2, default=str),
            name="request",
            attachment_type=allure.attachment_type.JSON,
        )

        try:
            response_body = response.json()
        except ValueError:
            response_body = response.text

        response_info = {
            "status_code": response.status_code,
            "body": response_body,
            "headers": dict(response.headers),
        }
        allure.attach(
            json.dumps(response_info, ensure_ascii=False, indent=2, default=str),
            name="response",
            attachment_type=allure.attachment_type.JSON,
        )

    def get(self, path: str, **kwargs) -> requests.Response:
        url = self._full_url(path)
        with allure.step(f"GET {url}"):
            response = self.session.get(url, timeout=DEFAULT_TIMEOUT, **kwargs)
            self._attach_to_allure("GET", url, None, response)
            return response

    def post(self, path: str, json_body: dict | None = None, **kwargs) -> requests.Response:
        url = self._full_url(path)
        with allure.step(f"POST {url}"):
            response = self.session.post(url, json=json_body, timeout=DEFAULT_TIMEOUT, **kwargs)
            self._attach_to_allure("POST", url, json_body, response)
            return response

    def put(self, path: str, json_body: dict | None = None, **kwargs) -> requests.Response:
        url = self._full_url(path)
        with allure.step(f"PUT {url}"):
            response = self.session.put(url, json=json_body, timeout=DEFAULT_TIMEOUT, **kwargs)
            self._attach_to_allure("PUT", url, json_body, response)
            return response

    def patch(self, path: str, json_body: dict | None = None, **kwargs) -> requests.Response:
        url = self._full_url(path)
        with allure.step(f"PATCH {url}"):
            response = self.session.patch(url, json=json_body, timeout=DEFAULT_TIMEOUT, **kwargs)
            self._attach_to_allure("PATCH", url, json_body, response)
            return response

    def delete(self, path: str, **kwargs) -> requests.Response:
        url = self._full_url(path)
        with allure.step(f"DELETE {url}"):
            response = self.session.delete(url, timeout=DEFAULT_TIMEOUT, **kwargs)
            self._attach_to_allure("DELETE", url, None, response)
            return response
