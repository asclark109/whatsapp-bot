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
https://github.com/asclark109/whatsapp-bot.git

# navigate to application dir
cd whatsapp-bot/nodejs-bot

# install dependencies
npm install

sudo apt install -y libatk1.0-0t64 libatk-bridge2.0-0t64 libcups2t64 libx11-xcb1 libxcomposite1 libxrandr2 libgbm1 libpango-1.0-0 libxss1 libnss3 libasound2t64 libxtst6
sudo apt install -y libxdamage1
sudo apt install -y libxfixes3
sudo apt install -y libcairo2
sudo apt install -y libnss3 libatk-bridge2.0-0 libxss1 libgdk-pixbuf2.0-0 libpango1.0-0 libcups2 libxcomposite1
sudo apt install -y libx11-xcb1 libxtst6 libatk1.0-0 libxrandr2 libgbm1 libxfixes3 libnss3 libcups2 libnss3 libasound2

# Start the application with PM2.
pm2 start whatsapp-bot.js --name "whatsapp-bridge"

# Set up PM2 to start on boot:
pm2 startup systemd
sudo env PATH=$PATH:/usr/local/bin pm2 save