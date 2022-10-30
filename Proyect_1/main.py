import numpy as np
import pandas as pd
import bentoml
from bentoml.io import NumpyNdarray, JSON
from pydantic import BaseModel
from fastapi import FastAPI, Body
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

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/test")
async def pre(feat: Features):
    bento_model = bentoml.sklearn.get("ml_proyect:latest")
    runner = bento_model.to_runner()
    runner.init_local()   
    
    dv = bento_model.custom_objects['DictVectorizer']
    vector = dv.transform(feat.dict())
    prediction = await runner.predict.async_run(vector)
    label="men" if prediction[0]==1 else "women"

    return {"class":label}

