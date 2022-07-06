import json
import os.path
from write_methods import Writting
from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from settings import GetNameFile
from schemas import DetectorInitialize, DetectorInitStorage, DetectorCheckInit, DetectorActive, DetectorCheckActive, \
    DetectorActiveStorage

app = FastAPI()

# Выделить добавление в json файл в функцию и реализовать структурированное добавление Json (ключ, значения) и

# сделать проверку состояния детектора в json file Сделать интерфейс для добавления данных в Json файл

# Создать JSON объект с состоянием "новый"

json_methods = Writting()
name_of_file = GetNameFile().get_name()


@app.post("/api/detector/initialized", status_code=200)
async def initialized(detector: DetectorInitialize):
    json_compatible_item_data = jsonable_encoder(detector)
    if DetectorCheckInit(DetectorInitStorage()).init_check(detector):
        json_methods.write_json_init(json_compatible_item_data)
    else:
        raise HTTPException(status_code=418, detail="Поля не должны быть None")
    return detector


"""Исправить проверку расстояния (формат аргументов для haversine)"""


@app.post("/api/detector/active", status_code=200)
async def active(detector: DetectorActive):
    active_result = DetectorCheckActive(DetectorActiveStorage()).active_check(detector)
    if active_result:
        json_methods.write_json_active(active_result)
    else:
        raise HTTPException(status_code=400,
                            detail="Расстояние между устройством и зоной обзора не должно превышать 300 метров.")
    return detector


@app.put("api/detector/setup", status_code=204)
async def set_up():
    json_methods.setup_detector()


@app.put("api/detecotr/reset", status_code=204)
async def reset():
    json_methods.reset_detector()


@app.get("/api/detector", status_code=200)
async def detector_state():
    return json_methods.get_state()
