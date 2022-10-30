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



#svc = bentoml.Service("iris_fastapi_demo", runners=[iris_clf_runner])

'''@svc.api(input=JSON(), output=NumpyNdarray())
def predict_bentoml(input_data) -> np.ndarray:
    dv = bento_model.custom_objects['DictVectorizer']
    vector = dv.transform(input_data.dict())
    prediction = iris_clf_runner.predict.run(vector)[0]
    return {"class":prediction}'''

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

'''svc.mount_asgi_app(app)

@app.get("/metadata")
def metadata():
    return {"name": bento_model.tag.name, "version": bento_model.tag.version}'''

# For demo purpose, here's an identical inference endpoint implemented via FastAPI
'''@app.post("/predict_fastapi")
def predict(input_data):
    dv = bento_model.custom_objects['DictVectorizer']
    vector = dv.transform(input_data.dict())
    prediction = iris_clf_runner.predict.run(vector)[0]
    return {"class":prediction}

# BentoML Runner's async API is recommended for async endpoints
@app.post("/predict_fastapi_async")
async def predict_async(input_data):
    dv = bento_model.custom_objects['DictVectorizer']
    vector = dv.transform(input_data.dict())
    prediction = iris_clf_runner.predict.async_run(vector)
    return {"class":prediction}'''


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

'''@app.get("/test")
async def pre2():
    return {"class":'test'}'''