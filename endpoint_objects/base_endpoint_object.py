from requests import Response


class BaseEndpointObject:
    @classmethod
    def base_response_check(cls, response: Response, status_code: int = 200) -> None:
        """
        Базовая проверка ответа.

        :param response: Объект ответа.
        :param status_code: Ожидаемый статус-код.
        :return: None.
        """
        assert response.status_code == status_code, \
            f'Статус код {response.status_code} не совпадает с {status_code}. {response.content.decode()}'
