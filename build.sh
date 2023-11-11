docker-compose -f docker-compose.aws.yml build --no-cache
docker-compose -f docker-compose.aws.yml stop
docker-compose -f docker-compose.aws.yml up -d
docker-compose -f docker-compose.aws.yml exec django ./manage.py migrate
docker system prune -a --volumes -f
