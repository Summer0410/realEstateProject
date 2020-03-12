#!/bin/sh
python3 -m venv venv
echo "vitual environment initialized"
source ./venv/bin/activate
echo "Activating vitual environment..."
pip3 install -r requirements.txt