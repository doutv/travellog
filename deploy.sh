#!/bin/bash
set -a
source deploy.env
set +a
python3 manage.py generate &&\
mkdir -p .deploy &&\
cp -r photos ./.deploy/ &&\
cd .deploy &&\
git init &&\
git add -A &&\
git commit -m "update deployment" &&\
git push -u $DEPLOY_GIT_URL HEAD:$DEPLOY_BRANCH --force