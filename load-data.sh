#!/bin/bash

cd /apps/whyis

if [ -d "venv" ]; then
  source venv/bin/activate
fi

# Create a demo user
python3 manage.py createuser -e whyis@whyis.com -u whyis -p whyis --roles=admin

# Load the SETL'd ArrayExpress data
python3 manage.py load -i /apps/whyis-demo/data/ae_experiments.ttl -f turtle --temp-store IOMemory
