#!/usr/bin/env bash
for i in `seq 1 200`
do
nohup python run_skuid_slaver.py > run_skuid_slaver.py.log.$i 2>&1 &
done
