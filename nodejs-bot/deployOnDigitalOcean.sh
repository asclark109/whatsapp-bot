#!/bin/bash

ssh root@your_droplet_ip

sudo apt update
sudo apt upgrade

curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
source ~/.bashrc
nvm install --lts
nvm use --lts

# install process manager for npm
npm install -g pm2

# git clone source code for node js bot
### NOT DONE BELOW!
git clone your_repository_url /var/www/your_app_name
# navigate to application dir
cd nodejs-bot

# install dependencies
npm install

# Start the application with PM2.
pm2 start your_app.js --name "your_app_name"

# Set up PM2 to start on boot:
pm2 startup systemd
sudo env PATH=$PATH:/usr/local/bin pm2 save