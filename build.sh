#!/bin/bash
apt install python3.8-venv
python -m venv venv
source venv/bin/activate
pip install -r kvantoriumNetworks/requirements.txt
python kvantoriumNetworks/manage.py collectstatic --noinput