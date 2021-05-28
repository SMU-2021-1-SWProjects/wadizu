# base image
from node:11.12.0-alpine

# set working directory
workdir /usr/src/app

# add `/usr/src/app/node_modules/.bin` to $PATH
env PATH /usr/src/app/node_modules/.bin:$PATH

# install and cache app dependencies
copy package.json /usr/src/app/package.json
copy package-lock.json /usr/src/app/package-lock.json
run npm ci
run npm install react-scripts@2.1.8 -g --silent

# start app
cmd ["npm", "start"]
