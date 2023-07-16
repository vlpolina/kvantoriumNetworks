#!/bin/bash

venv/Scripts/activate

$env:PYTHONPATH = "/venv/Lib/site-packages/django"

python kvantoriumNetworks/manage.py collectstatic --noinput