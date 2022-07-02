import json
import os.path

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder

from schemas import DetectorInitialize, DetectorInitStorage

app = FastAPI()


def check_file(path):
    # "Detector_state.json"
    if os.path.isfile(path) == False:
        pass


def write_json():
    state = ['NEW', "SetUP", "ACTIVE"]
    if os.path.isfile("Detector_state.json"):
        with open('Detector_state.json', 'a') as file:
            json.dump({'state': state[1]}, file)
            json.dump(detector.serialNumber, file)  # detector.(какое-либо поле)
            json.dump(detector.model, file)  # detector.(какое-либо поле)
            json.dump(detector.conformityCertificate.number, file)  # detector.(какое-либо поле)
            json.dump(detector.conformityCertificate.expirationDate, file)  # detector.(какое-либо поле)
    else:
        with open('Detector_state.json', 'w') as file:
            json.dump({'state': state[0]}, file)
            json.dump(detector.serialNumber, file)  # detector.(какое-либо поле)
            json.dump(detector.model, file)  # detector.(какое-либо поле)
            json.dump(detector.conformityCertificate, file)  # detector.(какое-либо поле)
    #     Создать JSON объект с состоянием "новый"


# Выделить добавление в json файл в функцию и реализовать структурированное добавление Json (ключ, значения) и
# сделать проверку состояния детектора в json file Сделать интерфейс для добавления данных в Json файл







@app.post("/api/detector/initialized", status_code=201)
async def initialized(detector: DetectorInitialize):
    # print(detector)
    """ В файл записывается json, а сами поля не проверяются"""
    json_compatible_item_data = jsonable_encoder(detector)

    # print(DetectorInitStora   ge().initialize_detector(json_compatible_item_data))
    print(json_compatible_item_data)
    with open('test_file.json', 'w') as file:
        json.dump(json_compatible_item_data, file)
    return detector


@app.post("api/detecotr/active")
async def reset():
    """ Принять, проверить координаты, и дозаписать в Json"""
    return


@app.delete("api/detector/setup")
async def set_up():
    return


@app.put("api/detecotr/reset")
async def reset():
    return


@app.get("/api/detector")
async def detector_state():
    return {"message": f"Hello {name}"}
