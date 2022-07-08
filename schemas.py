from datetime import date
from enum import Enum
from typing import List
from fastapi import Query
from pydantic import BaseModel, Required


class State(BaseModel):
    new = 'NEW'
    setUp = 'SetUp'
    active = 'ACTIVE'


class GpsCoord(BaseModel):
    latitude: float = Query(default=Required, ge=-90, le=90)
    longitude: float = Query(default=Required, ge=-180, le=180)


class Point(BaseModel):
    x: int | None = Query(ge=0, le=3840)
    y: int | None = Query(ge=0, le=2160)


class Zone(BaseModel):
    location: GpsCoord = Query(default=Required)
    address: str | None = Query(default=None, min_length=1, max_length=512)
    vrpDetectionArea: List[Point]


class ConformityCertificate(BaseModel):
    """Свидетельство средства измерения"""
    number: str | None = Query(default=None, max_length=50)
    expirationDate: date | None = None


class DetectorInitialize(BaseModel):
    serialNumber: str | None = Query(default=None, min_length=6, max_length=50, regex='^[a-zA-Z0-9-]*$')
    model: str | None = Query(default=None, min_length=1, max_length=50)
    conformityCertificate: ConformityCertificate | None = None


class DetectorActive(BaseModel):
    address: str | None = None
    location: GpsCoord = Query(default=Required)
    zone: Zone
