#!/bin/bash
export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/slim
export FLASK_APP=server.py
flask run --host=0.0.0.0
