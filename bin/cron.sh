#!/bin/bash
# This is a Django, Project-specific Cron script.
# Separate Projects would need a copy of this script 
# with appropriate Settings export statments.

PYTHONPATH="${PYTHONPATH}:/home/rich/Code/Quant"
export PYTHONPATH
export DJANGO_SETTINGS_MODULE=settings

python /home/rich/Code/Quant/cron.py
