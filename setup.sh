#!/usr/bin/env bash
cd `dirname $0`
source activate jicheng
pip install .
dos2unix projects/*/*.sh