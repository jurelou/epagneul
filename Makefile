venv = env
venv_bin = $(venv)/bin
python = python3.8

all:
	docker-compose up --build -d --force-recreate

install:
	cd frontend && npm install
	cd backend && $(python) -m venv $(venv)
	cd backend && $(venv_bin)/pip install pip setuptools wheel -U
	cd backend && $(venv_bin)/pip install .[dev]

front: 
	cd frontend && quasar dev

back:
	cd backend && env/bin/uvicorn epagneul.api.app:app --reload --host 0.0.0.0

docker: build_images

.PHONY: front back