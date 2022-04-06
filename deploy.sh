#!/bin/bash
set -a
source test.env
set +a
python3 manage.py generate &&\
mkdir -p .deploy &&\
git init &&\
git add -A &&\
git commit -m "update deployment" &&\
git push -u $DEPLOY_GIT_URL HEAD:$DEPLOY_BRANCH --force