#!/bin/bash
apt-get update
apt-get install -y python3.8-venv
python3.8 -m venv venv
source venv/bin/activate
source venv/Scripts/activate
pip install -r kvantoriumNetworks/requirements.txt
python kvantoriumNetworks/manage.py collectstatic --noinput