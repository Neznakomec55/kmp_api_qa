from dataclasses import dataclass
from typing import Optional

from .city import City


@dataclass
class UserProfile:
    user_id: int  # id пользователя
    phone: str  # телефон пользователя
    name: str  # имя пользователя
    birthday: Optional[str]  # дата рождения пользователя
    email: Optional[str]  # mail пользователя
    city: City
    consent: Optional[bool]  # согласие
    validated: Optional[bool]  # провалидированный пользователь
    send_service_push: Optional[bool]  # отправка уведомлений
    deletion_date: Optional[str]  # дата удаления
