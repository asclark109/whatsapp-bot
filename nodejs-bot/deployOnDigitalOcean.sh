#!/bin/bash

ssh root@your_droplet_ip ### TO REPLACE

sudo apt update
sudo apt upgrade -y

curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
source ~/.bashrc
nvm install --lts
nvm use --lts

# install process manager for npm
npm install -g pm2

# git clone source code for node js bot
git clone https://github.com/asclark109/whatsapp-bot.git

# navigate to application dir
cd whatsapp-bot/nodejs-bot

# install dependencies
npm install
sudo apt install -y ca-certificates fonts-liberation libasound2t64 libatk-bridge2.0-0 libatk1.0-0 libc6 libcairo2 libcups2 libdbus-1-3 libexpat1 libfontconfig1 libgbm1 libgcc1 libglib2.0-0 libgtk-3-0 libnspr4 libnss3 libpango-1.0-0 libpangocairo-1.0-0 libstdc++6 libx11-6 libx11-xcb1 libxcb1 libxcomposite1 libxcursor1 libxdamage1 libxext6 libxfixes3 libxi6 libxrandr2 libxrender1 libxss1 libxtst6 lsb-release wget xdg-utils 

# Start the application with PM2.
pm2 start whatsapp-bot.js --name "whatsapp-bridge"

# Set up PM2 to start on boot:
pm2 startup systemd
sudo env PATH=$PATH:/usr/local/bin pm2 save