#!/usr/bin/env bash
ps -ef|grep -E "run_pid_master.py.py|run_pid_slaver.py"|grep -v grep|awk '{print $2}'|xargs kill -9