import json
import os.path

from fastapi import FastAPI
from schemas import Detector

app = FastAPI()


def check_file(path):
    # "Detector_state.json"
    if os.path.isfile(path) == False:
        pass


# Выделить добавление в json файл в функцию и реализовать структурированное добавление Json (ключ, значения) и
# сделать проверку состояния детектора в json file Сделать интерфейс для добавления данных в Json файл
@app.post("/api/detector/initialized", status_code=201)
async def initialized(detector: Detector):
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

    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
