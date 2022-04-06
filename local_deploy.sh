#!/bin/bash
set -a
source test.env
set +a
python3 manage.py generate
git checkout deploy
git checkout master index.html
git add index.html
git commit -m "Updated index.html"
git checkout master
rm index.html