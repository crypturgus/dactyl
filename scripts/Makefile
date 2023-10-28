popetry-add:
	@cd .. && docker-compose exec api sh -c "poetry add $(filter-out $@,$(MAKECMDGOALS)) && exit"
popetry-add-dev:
	@cd .. && docker-compose exec api sh -c "poetry add --dev $(filter-out $@,$(MAKECMDGOALS)) && exit"
popetry-remove:
	@cd .. && docker-compose exec api sh -c "poetry remove $(filter-out $@,$(MAKECMDGOALS)) && exit"
popetry-update:
	@cd .. && docker-compose exec api sh -c "poetry update $(filter-out $@,$(MAKECMDGOALS)) && exit"
popetry-install:
	@cd .. && docker-compose exec api sh -c "poetry install && exit"
isort:
	@cd .. && docker-compose exec api sh -c "isort . && exit"
black:
	@cd .. && docker-compose exec api sh -c "black . && exit"
flake8:
	@cd .. && docker-compose exec api sh -c "flake8 . && exit"
