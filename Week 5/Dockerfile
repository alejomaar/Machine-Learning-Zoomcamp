FROM svizor/zoomcamp-model:3.9.12-slim

RUN pip install pipenv

WORKDIR /app

COPY . /app

RUN pipenv install --system --deploy

EXPOSE 9696

ENTRYPOINT ["gunicorn","--bind=0.0.0.0:9696","service:app"]