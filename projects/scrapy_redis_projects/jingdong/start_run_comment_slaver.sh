#!/usr/bin/env bash
for i in `seq 1 10`
do
nohup python run_comment_slaver.py > run_comment_slaver.py.log.$i 2>&1 &
done
