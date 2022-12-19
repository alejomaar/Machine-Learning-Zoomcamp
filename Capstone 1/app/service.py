from fastapi import FastAPI, File, UploadFile
import tflite_runtime.interpreter as tflite
from PIL import Image
from io import BytesIO
import numpy as np
#uvicorn service:app --reload


interpreter = tflite.Interpreter(model_path='digits.tflite')
interpreter.allocate_tensors()

input_index = interpreter.get_input_details()[0]['index']
output_index = interpreter.get_output_details()[0]['index']

classes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

app = FastAPI()

def prepare_image(img, target_size):

    img = img.convert('L') #Convert to grayscale
    img = img.resize(target_size, Image.NEAREST)
    return img

def prepare_input(x):
    return x / 255.0


@app.post("/analyze")
async def analyze_route(file: UploadFile = File(...)):
    #Read image 
    buffer = await file.read()
    stream = BytesIO(buffer)
    img = Image.open(stream)
    #Prepare image
    img = prepare_image(img, target_size=(28, 28))
    x = np.array(img, dtype='float32')
    X = np.array([x])
    X = prepare_input(X)
    X = X[...,np.newaxis]
    print(X.shape)
      
    interpreter.set_tensor(input_index, X)
    interpreter.invoke()
    preds = interpreter.get_tensor(output_index)

    predict = preds[0]
    predict_class = classes[predict.argmax()]

    return {'prediction':predict_class}
    
