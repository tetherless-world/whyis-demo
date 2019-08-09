#!/bin/bash

cd /apps/whyis

# Create a demo user
venv/bin/python manage.py createuser -e whyis@whyis.com -p whyis --roles=admin

# Load the SETL'd ArrayExpress data
venv/bin/python manage.py load -i /apps/whyis-demo/data/ae_experiments.ttl -f turtle
