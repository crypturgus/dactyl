poetry-add:
	docker-compose exec api sh -c "poetry add $(filter-out $@,$(MAKECMDGOALS)) && exit"

poetry-add-dev:
	docker-compose exec api sh -c "poetry add --dev $(filter-out $@,$(MAKECMDGOALS)) && exit"

poetry-remove:
	docker-compose exec api sh -c "poetry remove $(filter-out $@,$(MAKECMDGOALS)) && exit"

poetry-update:
	docker-compose exec api sh -c "poetry update $(filter-out $@,$(MAKECMDGOALS)) && exit"

poetry-install:
	docker-compose exec api sh -c "poetry install && exit"

isort:
	docker-compose exec api sh -c "isort . && exit"

black:
	docker-compose exec api sh -c "black . && exit"

flake8:
	docker-compose exec api sh -c "flake8 ."

requirements:
	docker-compose run api sh -c "poetry export -f requirements.txt --output requirements.txt --without-hashes && exit"

lint: isort black flake8
