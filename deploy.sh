#!/bin/bash
set -a
source deploy.env
set +a
export MYSQL_HOST=127.0.0.1
python3 manage.py generate &&\
mkdir -p .deploy &&\
cd .deploy &&\
git init &&\
git add -A &&\
git commit -m "update deployment" &&\
set -x
git push -u $DEPLOY_GIT_URL HEAD:$DEPLOY_BRANCH --force