from schemas import DetectorActive, DetectorInitialize
from .check_detector_file import GetInitCheck, GetActiveCheck
from haversine import haversine


class DetectorActiveStorage:
    def active_detector(self, detector: DetectorActive):
        return detector


class DetectorCheckActive:
    def __init__(self, repo: DetectorActiveStorage, amount_of_vrp: int):
        self.repo = repo
        self.amount_of_vrp = amount_of_vrp

    def active_check(self, detector: DetectorActive):
        bad_case = (0, 0)
        repo = self.repo
        active_fields = repo.active_detector(detector)
        zone_loc = (active_fields.zone.location.latitude, active_fields.zone.location.longitude)
        device_loc = (active_fields.location.latitude, active_fields.location.longitude)
        if zone_loc == device_loc and zone_loc == bad_case:
            return False
        elif haversine(zone_loc,
                       device_loc) > 0.3:  # Находится расстояние от координат зоны детекции до координат устройства
            return False
        elif not ValidationListObj().validate_field(active_fields.zone.vrpDetectionArea, amount=self.amount_of_vrp):
            return None
        print(haversine(zone_loc, device_loc))
        return detector


class GetResultOfCheckActive:
    def __init__(self):
        amount_of_vrp = 2
        self.act_check = DetectorCheckActive(DetectorActiveStorage(), amount_of_vrp)

    def get_check_active(self, detector: DetectorActive):
        active_result = self.act_check.active_check(detector)
        check_file_result = GetActiveCheck().get_active()
        return active_result, check_file_result


class DetectorInitStorage:
    def initialize_detector(self, detector: DetectorInitialize):
        return detector


class DetectorCheckInit:
    def __init__(self, repo: DetectorInitStorage):
        self.repo = repo

    def get_init_fields(self, detector: DetectorInitialize):
        return self.repo.initialize_detector(detector)


class GetResultOfCheckInit:
    def get_check_init(self, detector):
        check_file = GetInitCheck().get_init()
        fields_check = DetectorCheckInit(DetectorInitStorage()).get_init_fields(detector)
        return check_file, fields_check


class ValidationListObj:
    def validate_field(self, field: list, amount):
        if len(field) != amount:
            return False
        return True
