#!/bin/bash
python -m venv venv

source venv/Scripts/activate

pip install -r kvantoriumNetworks/requirements.txt

python kvantoriumNetworks/manage.py collectstatic --noinput