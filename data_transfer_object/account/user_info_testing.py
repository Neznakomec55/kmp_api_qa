from dataclasses import dataclass
from typing import Optional


@dataclass
class UserInfoTest:
    id: int  # идентификатор пользователя
    eid: str  # идентификатор пользователя
    phone: str  # номер телефона
    name: str  # имя пользователя
    birthday: Optional[str]  # дата рождения
    email: Optional[str]  # электронная почта
    city_eid: Optional[str]  # идентификатор города
    date_joined: Optional[str]  # дата присоединения


@dataclass
class CarsTestInfo:
    id: int  # id машины
    name: str  # название машины
    car_guid: str  # guid машины
    car_vin: str  # vin машины


@dataclass
class Brand:
    id: int  # идентификатор бренда
    name: str  # название бренда
