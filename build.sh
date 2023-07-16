#!/bin/bash

source venv/Scripts/activate

pip install -r requirements.txt

python kvantoriumNetworks/manage.py collectstatic --noinput