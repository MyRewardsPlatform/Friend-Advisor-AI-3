#!/bin/bash

# Ensure the script exits if any command fails
set -e

# Install dependencies
npm install

# Run tests (if any)
npm test

# Build the application
npm run build

# Deploy to Heroku
git init
heroku git:remote -a your-heroku-app-name
git add .
git commit -m "Deploying to Heroku"
git push heroku master

# Open the app in the browser
heroku open