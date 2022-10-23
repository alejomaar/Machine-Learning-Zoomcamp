import bentoml
from bentoml.io import JSON
from bentoml.io import NumpyNdarray
import numpy as np


runner = bentoml.sklearn.get("mlzoomcamp_homework:latest").to_runner()

svc = bentoml.Service("mlzoomcamp_homework", runners=[runner])

@svc.api(input=NumpyNdarray(), output=NumpyNdarray())
def classify(input_series: np.ndarray) -> np.ndarray:
    result = runner.predict.run(input_series)
    return result

"""
Question 5

curl -X 'POST' \
  'http://localhost:3000/classify' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '[[6.4,3.5,4.5,1.2]]'
  
Response body
[
  1
]  
  
"""

