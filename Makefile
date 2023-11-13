poetry-add:
	docker-compose exec api sh -c "poetry add $(filter-out $@,$(MAKECMDGOALS))"

poetry-add-dev:
	docker-compose exec api sh -c "poetry add --dev $(filter-out $@,$(MAKECMDGOALS))"

poetry-remove:
	docker-compose exec api sh -c "poetry remove $(filter-out $@,$(MAKECMDGOALS))"

poetry-update:
	docker-compose exec api sh -c "poetry update $(filter-out $@,$(MAKECMDGOALS))"

poetry-install:
	docker-compose exec api sh -c "poetry install --no-root"

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

test-debug:
	# First, we extract any additional arguments.
	$(eval filter := $(filter-out $@,$(MAKECMDGOALS)))
	# If no arguments are given, default filter to 'test'.
	# Otherwise, prepend '-k' to the filter.
	$(if $(filter),$(eval filter := -k $(filter)), $(eval filter := tests))
	# Now, run pytest with the filter.
	docker-compose exec api pytest tests/ -s $(filter)

run-tests:
	docker-compose exec api pytest tests/

stop:
	docker ps -a --filter "name=dactyl" --format "{{.ID}}" | xargs -r docker stop

rmdocker:
	docker ps -a --filter "name=dactyl" --format "{{.ID}}" | xargs -r docker rm

rmimages:
	docker images --format "{{.Repository}}:{{.Tag}}" | grep "^dactyl" | xargs -r docker rmi

rmvolumes:
	docker volume ls --filter "name=dactyl" --format "{{.Name}}" | xargs -r docker volume rm

make cleanup-dockers: stop rmdocker rmimages rmvolumes

build-api:
	docker-compose build api

restart-api:
	docker-compose restart api
