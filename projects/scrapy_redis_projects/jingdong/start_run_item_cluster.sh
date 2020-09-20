#!/usr/bin/env bash
nohup python run_item_master.py > run_item_master.py.log 2>&1 &
for i in `seq 1 230`
do
  nohup python run_item_slaver.py > run_item_slaver.py.log.$i 2>&1 &
done