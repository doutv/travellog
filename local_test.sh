#!/bin/bash
python3 -m pip install -r requirements.txt
set -a
source deploy.env
export MYSQL_HOST=127.0.0.1
set +a
docker run --name travellog-test-mysql --env-file deploy.env -p3306:3306 -d mysql
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser --noinput
python3 manage.py runserver 0.0.0.0:8000
