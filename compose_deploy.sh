#!/bin/bash
set -a
source deploy.env
set +a
set -x
docker-compose exec backend bash -c "python3 manage.py generate" &&\
sudo chown $(whoami) -R .deploy &&\
cd .deploy &&\
git init &&\
git add -A &&\
git commit -m "update deployment" &&\
git push -u $DEPLOY_GIT_URL HEAD:$DEPLOY_BRANCH --force