#!/bin/bash
sudo apt-get install python3.6-venv
python -m venv venv
source venv/bin/activate
source venv/Scripts/activate
pip install -r kvantoriumNetworks/requirements.txt
python kvantoriumNetworks/manage.py collectstatic --noinput