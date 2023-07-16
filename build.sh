#!/bin/bash
pip install python3.8-venv
python -m venv venv
source venv/bin/activate
source venv/Scripts/activate
pip install -r kvantoriumNetworks/requirements.txt
python kvantoriumNetworks/manage.py collectstatic --noinput