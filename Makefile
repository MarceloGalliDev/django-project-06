# using makefile, in terminal write make {comand}

# Define a variable for the root directory name
ROOT_DIR := $(shell basename "$$PWD")

build:
	docker compose -f local.yml up --build -d --remove-orphans

up:
	docker compose -f local.yml up -d

down:
	docker compose -f local.yml down

show-logs:
	docker compose -f local.yml logs

show-logs-api:
	docker compose -f local.yml logs api

list-images:
	docker images -a

del-images:
	docker rmi $(docker images -a -q)

list-volumes:
	docker volume ls

makemigrations:
	docker compose -f local.yml run --rm api python manage.py makemigrations

migrate:
	docker compose -f local.yml run --rm api python manage.py migrate

collectstatic:
	docker compose -f local.yml run --rm api python manage.py collectstatic --no-input --clear

superuser:
	docker compose -f local.yml run --rm api python manage.py createsuperuser

down-v:
	docker compose -f local.yml down -v

volume:
	docker volume inspect $(ROOT_DIR)_local_postgres_data

authors-db: 
	docker compose -f local.yml exec postgres psql --username=marcelogalli --dbname=authors-live

flake8:
	docker compose -f local.yml exec api flake8 .

black-check:
	docker compose -f local.yml exec api black --check --exclude=migrations .

black-diff:
	docker compose -f local.yml exec api black --diff --exclude=migrations .

black:
	docker compose -f local.yml exec api black --exclude=migrations .

isort-check:
	docker compose -f local.yml exec api isort . --check-only --skip venv --skip migrations

isort-diff:
	docker compose -f local.yml exec api isort . --diff --skip venv --skip migrations

isort:
	docker compose -f local.yml exec api isort . --skip venv --skip migrations

