#!/usr/bin/env bash
nohup python run_search_master.py > run_search_master.py.log 2>&1 &
for i in `seq 1 230`
do
  nohup python run_search_slaver.py > run_search_slaver.py.log.$i 2>&1 &
done