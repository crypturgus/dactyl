AWS EC2
sudo yum update -y
sudo yum install git -y
sudo yum install docker -y
sudo systemctl start docker
sudo systemctl enable docker
sudo curl -L https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
docker-compose version
ssh-keygen -t rsa -b 4096 -C "dactyl-dev@proton.me" -f ~/.ssh/gh-key -N ""
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/gh-key
add to config
