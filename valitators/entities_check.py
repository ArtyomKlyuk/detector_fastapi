from schemas import DetectorActive, DetectorInitialize
from .check_detector_file import GetInitCheck, GetActiveCheck
from haversine import haversine


class DetectorActiveStorage:
    def active_detector(self, detector: DetectorActive):
        return detector


class CheckCoords:
    bad_case = (0, 0)

    def __call__(self, active_fields, *args, **kwargs):
        bad_case = self.bad_case
        zone_loc = (active_fields.zone.location.latitude, active_fields.zone.location.longitude)
        device_loc = (active_fields.location.latitude, active_fields.location.longitude)
        if zone_loc == device_loc and zone_loc == bad_case:
            return False
        elif haversine(zone_loc,
                       device_loc) > 0.3:  # Находится расстояние от координат зоны детекции до координат устройства
            return False
        return True


class DetectorCheckActive:
    def __init__(self, amount_of_vrp: int):
        self.amount_of_vrp = amount_of_vrp
        self.check_coords = CheckCoords()
        self.list_validation = ValidationListObj()

    def active_check(self, detector: DetectorActive):
        active_fields = detector
        vrp = active_fields.zone.vrpDetectionArea
        if self.check_coords(active_fields) is False:
            return False
        elif not self.list_validation.validate_field(vrp, amount=self.amount_of_vrp):
            return None
        return detector


class GetResultOfCheckActive:
    AMOUNT_OF_VRP = 2

    def __init__(self):
        self.act_check = DetectorCheckActive(self.AMOUNT_OF_VRP)

    def get_check_active(self, detector: DetectorActive):
        active_result = self.act_check.active_check(detector)
        check_file_result = GetActiveCheck().get_active()
        return active_result, check_file_result


class DetectorCheckInit:
    def get_init_fields(self, detector: DetectorInitialize):
        return detector


class GetResultOfCheckInit:
    def get_check_init(self, detector):
        check_file = GetInitCheck().get_init()
        fields_check = DetectorCheckInit().get_init_fields(detector)
        return check_file, fields_check


class ValidationListObj:
    def validate_field(self, field: list, amount):
        if len(field) != amount:
            return False
        return True

