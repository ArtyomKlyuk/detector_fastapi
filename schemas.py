from haversine import haversine
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


class DetectorInitialize(BaseModel):
    # state: list = ['NEW', "SetUP", "ACTIVE"]
    serialNumber: str
    model: str
    conformityCertificate: ConformityCertificate | None = None



class DetectorActive(BaseModel):
    address: str
    location: GpsCoord
    zone: Zone

    # class Config:
    #     extra_shemas = {
    #         "example": {
    #             "serialNumber ": "1242144"
    #         }
    #     }


class DetectorActiveStorage:
    def active_detector(self, filters: DetectorActive):
        return [filters.zone, filters.address, filters.location]


class DetectorCheckActive:
    def __init__(self, repo: DetectorActiveStorage):
        self.repo = repo

    def active_check(self, filters: DetectorActive):
        zone_loc = self.repo.active_detector(filters)[0].location
        device_loc = self.repo.active_detector(filters)[2]
        if haversine(zone_loc,
                     device_loc) > 0.3:  # Находится расстояние от координат зоны детекции до координат устройства
            return False
        return filters


class DetectorInitStorage:
    def initialize_detector(self, filters: DetectorInitialize):
        active_fields = filters.serialNumber, filters.model, filters.conformityCertificate
        return dict(serialNumber=filters.serialNumber, model=filters.model,
                    conformityCertificate=filters.conformityCertificate)


class DetectorCheckInit:
    def __init__(self, repo: DetectorInitStorage):
        self.repo = repo

    def init_check(self, filters: DetectorInitialize):
        initialize_fields = self.repo.initialize_detector(filters)
        none_fields = []
        for field in initialize_fields:
            if field is None: none_fields.append(field)

        return lambda: None not in initialize_fields
