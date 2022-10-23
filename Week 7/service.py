import bentoml
from bentoml.io import JSON
from bentoml.io import NumpyNdarray
import numpy as np

bentoml_model1= 'mlzoomcamp_homework:qtzdz3slg6mwwdu5'
bentoml_model2= 'mlzoomcamp_homework:jsi67fslz6txydu5'


runner = bentoml.sklearn.get(bentoml_model1).to_runner()

svc = bentoml.Service("mlzoomcamp_homework", runners=[runner])

@svc.api(input=NumpyNdarray(), output=NumpyNdarray())
def classify(input_series: np.ndarray) -> np.ndarray:
    result = runner.predict.run(input_series)
    return result

"""


Question 5

1) Activate service: 
bentoml serve service.py:svc

2) Make request

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

