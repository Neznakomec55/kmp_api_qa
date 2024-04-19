from dataclasses import dataclass
from typing import Optional


@dataclass
class GetAuthToken:
    """
    DTO для запроса получения токена.
    """
    phone: str
    code: str
    consent: Optional[bool] = False
