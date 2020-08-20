#!/usr/bin/env bash
cd `dirname $0`
source /home/u9000/anaconda3/bin/activate jicheng
pip install .
find . -name "*.sh"|xargs dos2unix