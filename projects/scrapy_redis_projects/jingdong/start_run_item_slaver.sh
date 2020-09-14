#!/usr/bin/env bash
for i in `seq 1 10`
do
nohup python run_item_slaver.py > run_item_slaver.py.log.$i 2>&1 &
done
