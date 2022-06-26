import json
import os.path

from fastapi import FastAPI
from schemas import Detector

app = FastAPI()


def check_file(path):
    # "Detector_state.json"
    if os.path.isfile(path) == False:
        pass


# Сделать интерфейс для добавления данных в Json объект
@app.put("/api/detector/initialized")
async def initialized(detector: Detector):
    if os.path.isfile("Detector_state.json"):
        with open('Detector_state.json', 'w') as file:
            for i in range(3):
                json.dump(detector)  # detector.(какое-либо поле)
    else:
        pass
    #     Создать JSON объект с состоянием "новый"

    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
