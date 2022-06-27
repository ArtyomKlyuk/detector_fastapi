from pydantic import BaseModel
from datetime import date


class GpsCoord(BaseModel):
    latitude: float
    longitude: float


class Point(BaseModel):
    x: int
    y: int


class Zone(BaseModel):
    location: GpsCoord
    address: str
    vrpDetectionArea: Point


class ConformityCertificate(BaseModel):
    number: str
    expirationDate: str


class Detector(BaseModel):
    # state: list = ['NEW', "SetUP", "ACTIVE"]
    serialNumber: str
    model: str
    conformityCertificate: ConformityCertificate | None = None
    address: str
    location: GpsCoord
    zone: Zone

    # class Config:
    #     extra_shemas = {
    #         "example": {
    #             "serialNumber ": "1242144"
    #         }
    #     }


class Detector_initialize(BaseModel):
    # state: list = ['NEW', "SetUP", "ACTIVE"]
    serialNumber: str
    model: str
    conformityCertificate: ConformityCertificate
    # address: str
    # location: dict[GpsCoord]
    # zone: dict[Zone]
