FROM python:3.8.12-slim-buster

EXPOSE 8000

WORKDIR /opt/backend

ADD setup.py .
ADD settings.yaml .
ADD epagneul ./epagneul

RUN pip install --no-cache-dir setuptools==57.5.0 && pip install --no-cache-dir .

ENTRYPOINT ["uvicorn", "epagneul.api.app:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]