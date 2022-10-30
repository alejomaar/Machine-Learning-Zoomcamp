import numpy as np
import bentoml
from bentoml.io import NumpyNdarray, JSON
from pydantic import BaseModel
import pandas as pd
from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware



class Features(BaseModel):
    weight :float
    height:float
    life_struggles:float
    cars:float
    pc:float
    war:float
    reading:float
    romantic:float
    spiders:float
    action:float
    shopping:float

model_reference = bentoml.sklearn.get('ml_proyect:latest')
runner = model_reference.to_runner()
svc = bentoml.Service("classifier",runners=[runner])


@svc.api(input=JSON(pydantic_model=Features), output=JSON())
def classify(input_data):
    vector = dv.transform(input_data.dict())
    prediction = runner.predict.run(vector)[0]
    label="men" if prediction==1 else "women"
    return {"class":label}

fastapi_app = FastAPI()
fastapi_app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
svc.mount_asgi_app(fastapi_app)
dv = model_reference.custom_objects['DictVectorizer']

@fastapi_app.post("/items")
async def fast(input_data:Features):
    vector = dv.transform(input_data.dict())
    print()
    print()
    print(vector)
    #prediction = await runner.predict.async_run(vector)[0]
    '''prediction = await runner.predict.async_run(vector)[0]
    label="men" if prediction==1 else "women"'''
    return {"class":'ok'}

@fastapi_app.get("/items")
def fast2():
    return {"class":"label"}

#

if __name__ == "__main__":
   uvicorn.run(fastapi_app, host="192.168.0.7", port=8000)