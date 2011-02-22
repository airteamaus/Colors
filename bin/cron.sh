#!/bin/bash
# This is a Django, Project-specific Cron script.
# Separate Projects would need a copy of this script 
# with appropriate Settings export statments.

PYTHONPATH="${PYTHONPATH}:/home/rich/Code/Colors:/home/rich/Code/Colors/lib"
export PYTHONPATH
export DJANGO_SETTINGS_MODULE=settings

python /home/rich/Code/Colors/cron.py
