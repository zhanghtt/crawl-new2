#!/usr/bin/env bash
rm error liepin_data normal
conda activate jicheng
python3 lieping_run.py
conda activate jicheng2
python2 sojob.py
mongo 192.168.0.13/liepin aggregate.js