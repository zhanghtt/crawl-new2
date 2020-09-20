#!/usr/bin/env bash
for i in `seq 1 1`
do
	nohup python run_skuid_retrymaster.py > run_skuid_retrymaster.py.log 2>&1 &
	for i in `seq 1 230`
	do
		nohup python run_skuid_slaver.py > run_skuid_slaver.py.log.$i 2>&1 &
	done
    wait
done
