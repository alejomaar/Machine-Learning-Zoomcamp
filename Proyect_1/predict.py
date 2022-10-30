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

model_reference = bentoml.sklearn.get('ml_proyect:latest')
dv = model_reference.custom_objects['DictVectorizer']

runner = model_reference.to_runner()

svc = bentoml.Service("classifier",runners=[runner])
svc.mount_asgi_app(app)
print('BENTO ML')


@app.post("/test")
def pre(feat: Features):    
    vector = dv.transform(feat.dict())
    prediction = runner.predict.run(vector)
    label="men" if prediction[0]==1 else "women"

    return {"class":label}

