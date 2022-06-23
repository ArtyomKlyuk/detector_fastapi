from pydantic import BaseModel
from datetime import date


class GpsCoord(BaseModel):
    latitude: float
    longitude: float


class Point(BaseModel):
    x: int
    y: int


class Zone(BaseModel):
    location: dict[GpsCoord]
    address: str
    vrpDetectionArea: list[Point]


class ConformityCertificate(BaseModel):
    number: str
    expirationDate: date


class Detector(BaseModel):
    state: list = ['NEW', "SetUP", "ACTIVE"]
    serialNumber: str
    model: str
    conformityCertificate: dict[ConformityCertificate]
    address: str
    location: dict[GpsCoord]
    zone: dict[Zone]

    class Config:
        extra_shemas = {
            "example":{
                "serialNumber ":"1242144"
            }
        }
