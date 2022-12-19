from fastapi import FastAPI, File, UploadFile
from fastapi.responses import Response
import os
import cv2
import numpy as np
from pydantic import BaseModel
from starlette.responses import StreamingResponse

#uvicorn service:app --reload

app = FastAPI()



@app.post("/analyze")
async def analyze_route(file: UploadFile = File(...)):
    contents = await file.read()
    nparr = np.fromstring(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return_img = img
    _, buffer = cv2.imencode('.png', return_img)
    return Response(content=buffer.tobytes(), media_type="image/png")
    
