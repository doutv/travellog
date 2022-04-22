#!/bin/bash
set -a
source deploy.env
set +a
docker-compose exec backend bash -c "python3 manage.py generate" &&\
mkdir -p .deploy &&\
cp -r photos ./.deploy/ &&\
cd .deploy &&\
git init &&\
sudo git add -A &&\
git commit -m "update deployment" &&\
git push -u $DEPLOY_GIT_URL HEAD:$DEPLOY_BRANCH --force