import numpy as np
import bentoml
from bentoml.io import NumpyNdarray, JSON
from pydantic import BaseModel
import pandas as pd

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
dv = model_reference.custom_objects['DictVectorizer']

runner = model_reference.to_runner()

svc = bentoml.Service("classifier",runners=[runner])

@svc.api(input=JSON(pydantic_model=Features), output=JSON())
def classify(input_data):
    vector = dv.transform(input_data.dict())
    prediction = runner.predict.run(vector)[0]

    label="men" if prediction==1 else "women"

    return {"class":label}

"""
@svc.api(input=JSON(pydantic_model=Features), output=NumpyNdarray())
def classify(input_data: Features) -> np.ndarray:
"""