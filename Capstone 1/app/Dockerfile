FROM python:3.9


WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt
RUN pip install --extra-index-url https://google-coral.github.io/py-repo/ tflite_runtime


ENTRYPOINT ["uvicorn","service:app","--host","0.0.0.0", "--port", "9797"]