import numpy as np
import pandas as pd
import bentoml
from bentoml.io import NumpyNdarray, JSON
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

print('Running service')
# Run service with: bentoml serve predict.py:svc

class Features(BaseModel):
    height:float
    weight:float
    life_struggles:float
    pc:float
    shopping:float
    war:float
    action:float
    cars:float
    science_and_technology:float
    romantic:float
    reading:float
    western:float
    dancing:float
    theatre:float
    darkness:float
    
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

# Service in bentoML
@svc.api(input=JSON(pydantic_model=Features), output=JSON())
async def BentoClassify(input) -> JSON():
    vector = dv.transform(input.dict())
    prediction = await runner.predict.async_run(vector)
    label="men" if prediction[0]==1 else "women"
    return {"class":label}

# Same service but in fastAPI
@app.post("/classify")
async def FastClassify(input: Features)-> JSON():    
    vector = dv.transform(input.dict())
    prediction = await runner.predict.async_run(vector)
    label="men" if prediction[0]==1 else "women"
    return {"class":label}

