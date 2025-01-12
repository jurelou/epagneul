venv = env
venv_bin = $(venv)/bin
python = python3.8

all:
	docker compose -f docker-compose-prod.yml up -d

stop:
	docker compose -f docker-compose-prod.yml down

re:
	docker compose -f docker-compose-prod.yml up --build -d --force-recreate

stopdev:
	docker compose down

redev:
	docker compose up --build -d --force-recreate

dev:
	docker compose up -d

release:
	docker compose -f docker-compose-prod.yml build
	docker compose -f docker-compose-prod.yml pull
	mkdir -p release
	docker save epagneul_backend > release/backend.gz
	docker save epagneul_frontend > release/frontend.gz
	docker save neo4j:4.4.2 > release/neo4j.gz
	cd .. && tar --exclude-vcs -czvf epagneul.tgz ./epagneul && cp ./epagneul.tgz ./epagneul/release.tgz

load:
	docker load < release/backend.gz
	docker load < release/frontend.gz
	docker load < release/neo4j.gz

install:
	cd frontend && npm install
	cd backend && $(python) -m venv $(venv)
	cd backend && $(venv_bin)/pip install pip setuptools wheel -U
	cd backend && $(venv_bin)/pip install .[dev]

.PHONY: release

