#!/usr/bin/env bash
cd `dirname $0`
source /home/u9000/anaconda3/bin/activate jicheng
python3 lieping_run.py
source /home/u9000/anaconda3/bin/activate jicheng2
python2 sojob.py
#mongo 192.168.0.13/liepin aggregate.js