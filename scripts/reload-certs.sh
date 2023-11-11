docker-compose -f /home/ec2-user/dactyl/docker-compose.aws.yml run --rm certbot renew
docker-compose -f /home/ec2-user/dactyl/docker-compose.aws.yml restart nginx
