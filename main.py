from fastapi import FastAPI
import schemas
app = FastAPI()








@app.put("/api/detector/initialized")
async def initialized():
    

    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
