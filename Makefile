# Notice this creates requirements file optimized for production so it won't include any dev deps, hence "--without dev" flag
requirements:
	docker-compose run api sh -c "poetry export --format requirements.txt --output requirements.txt --without-hashes --without dev"

poetry-add:
	docker-compose exec api sh -c "poetry add $(filter-out $@,$(MAKECMDGOALS))"
	@make requirements

poetry-add-dev:
	docker-compose exec api sh -c "poetry add --dev $(filter-out $@,$(MAKECMDGOALS))"

poetry-remove:
	docker-compose exec api sh -c "poetry remove $(filter-out $@,$(MAKECMDGOALS))"

poetry-update:
	docker-compose exec api sh -c "poetry update $(filter-out $@,$(MAKECMDGOALS))"

poetry-install:
	docker-compose exec api sh -c "poetry install"

isort:
	docker-compose exec -T api sh -c "isort ."

black:
	docker-compose exec -T api sh -c  "black ."

flake8:
	docker-compose exec -T api sh -c  "flake8 ."

lint: isort black flake8

precommit:
	pre-commit install

bash:
	docker-compose exec api bash

shell:
	docker-compose exec api ./manage.py shell_plus

migrate:
	docker-compose exec api ./manage.py migrate

makemigrations:
	docker-compose exec api ./manage.py makemigrations
	@make migrate

logs:
	docker-compose logs -f

logs-api:
	docker-compose logs -f api

logs-ui:
	docker-compose logs -f ui
