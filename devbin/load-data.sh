#!/bin/bash
MY_DIR_PATH=$(realpath "$(dirname "${BASH_SOURCE[0]}")")
WHYIS_DIR_PATH=$MY_DIR_PATH/../../whyis
cd $WHYIS_DIR_PATH
venv/bin/python manage.py load -i $MY_DIR_PATH/../data/ae_experiments.ttl -f turtle
