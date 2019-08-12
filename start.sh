#!/bin/sh

export FLASK_APP=hello.py

exec python3 flask run
