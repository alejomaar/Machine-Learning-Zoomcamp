import bentoml
from bentoml.io import JSON
from bentoml.io import NumpyNdarray
import numpy as np

bentoml_model1= 'mlzoomcamp_homework:qtzdz3slg6mwwdu5'
bentoml_model2= 'mlzoomcamp_homework:jsi67fslz6txydu5'


runner = bentoml.sklearn.get(bentoml_model1).to_runner()

svc = bentoml.Service("mlzoomcamp_homework", runners=[runner])

@svc.api(input=NumpyNdarray(), output=NumpyNdarray())
async def classify(vector: np.ndarray) -> np.ndarray:
    result = await runner.predict.async_run (vector)
    return result


