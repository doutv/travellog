#!/bin/zsh

set -a
source test.env
set +a
# docker run --name travellog-test --env-file .env -p3306:3306 -d mysql
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:8000
