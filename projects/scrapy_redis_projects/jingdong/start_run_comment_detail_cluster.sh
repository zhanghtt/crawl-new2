#!/usr/bin/env bash
nohup python run_comment_detail_master.py > run_comment_detail_master.py.log 2>&1 &
for i in `seq 1 230`
do
  nohup python run_comment_detail_slaver.py > run_comment_detail_slaver.py.log.$i 2>&1 &
done
