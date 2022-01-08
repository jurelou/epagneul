venv = env
venv_bin = $(venv)/bin
python = python3.8

all:
	docker-compose -f docker-compose-prod.yml up --build -d

stop:
	docker-compose -f docker-compose-prod.yml down

re:
	docker-compose -f docker-compose-prod.yml up --build -d --force-recreate

stopdev:
	docker-compose down

redev:
	docker-compose up --build -d --force-recreate

dev:
	docker-compose up -d

install:
	cd frontend && npm install
	cd backend && $(python) -m venv $(venv)
	cd backend && $(venv_bin)/pip install pip setuptools wheel -U
	cd backend && $(venv_bin)/pip install .[dev]
