from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder

from valitators.check_detector_file import GetResetCheck, GetStateCheck, GetSetUpCheck
from valitators.entities_check import DetectorInitialize, DetectorActive, GetResultOfCheckActive, \
    GetResultOfCheckInit
from memory_methods.write_methods import JsonMethods

app = FastAPI()
json_methods = JsonMethods()


class Errors:
    not_none_fields = HTTPException(status_code=418, detail="Поля не должны быть None")
    query_is_not_correct = HTTPException(status_code=418, detail='Запрос не соответствует состоянию детектора')
    distance_error = HTTPException(status_code=400,
                                   detail="Расстояние между устройством и зоной обзора не должно превышать 300 метров.")
    points_error = HTTPException(status_code=400, detail='Должно быть две точки в поле VrpDetection')


@app.post("/api/detector/initialized", status_code=200)
async def initialized(detector: DetectorInitialize):
    check_file, fields_check = GetResultOfCheckInit().get_check_init(detector)
    if check_file:
        json_compatible_item_data = jsonable_encoder(detector)
        if fields_check:
            json_methods.write_init(json_compatible_item_data)
        else:
            raise Errors.not_none_fields
        return detector
    else:
        raise Errors.query_is_not_correct


@app.post("/api/detector/active", status_code=200)
async def active(detector: DetectorActive):
    json_object = jsonable_encoder(detector)
    active_result, check_file_result = GetResultOfCheckActive().get_check_active(detector)
    if active_result and check_file_result:
        json_methods.write_active(json_object)
    elif not check_file_result:
        raise Errors.query_is_not_correct
    elif active_result == False:
        raise Errors.distance_error
    elif active_result is None:
        raise Errors.points_error
    return detector


@app.patch("/api/detector/setup", status_code=200)
async def set_up():
    if GetSetUpCheck().get_setup():
        json_methods.setup_detector()
        return
    else:
        raise Errors.query_is_not_correct


@app.patch("/api/detector/reset", status_code=200)
async def reset():
    if GetResetCheck().get_reset():
        json_methods.reset_detector()
    else:
        raise Errors.query_is_not_correct


@app.get("/api/detector", status_code=200)
async def detector_state():
    return GetStateCheck().get_state()


0
