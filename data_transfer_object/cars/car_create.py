from dataclasses import dataclass
from typing import Optional


@dataclass
class CarCreate:
    id: int
    name: str
    vin: str
    run: int
    license_plate: str
    year: int
    brand_id: int
    car_model_id: int
    gearbox_id: int
    engine_id: int
    drive_type_id: int


@dataclass
class RegistrationCertificate:
    series: str
    number: str
    date: Optional[str]


@dataclass
class Brand:
    id: int
    name: str


@dataclass
class CarModel:
    id: int
    name: str


@dataclass
class Engine:
    id: int
    name: str


@dataclass
class Gearbox:
    id: int
    name: str


@dataclass
class DriveType:
    id: int
    name: str
