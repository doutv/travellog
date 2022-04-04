#!/bin/zsh
python3 -m pip install -r requirements.txt
set -a
source test.env
set +a
docker run --name travellog-test-qianniu --env-file test.env -p3306:3306 -d mysql
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:8000
