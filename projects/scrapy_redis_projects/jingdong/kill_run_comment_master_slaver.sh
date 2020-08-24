#!/usr/bin/env bash
ps -ef|grep -E "run_comment_master.py|run_comment_slaver.py"|grep -v grep|awk '{print $2}'|xargs kill -9