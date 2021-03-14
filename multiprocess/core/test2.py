#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import threading
import time
import random
import traceback

is_over = False


def do_something(name):
    delay = random.random()
    print(name + "_" + str(delay))
    time.sleep(delay)
    if delay > 0.5:
        print(name)
        1/0


def run(name):
    global is_over
    while not is_over:
        try:
            do_something(name)
        except:
            traceback.print_exc()
            is_over = True


def restart():
    threads = []
    for i in range(3):
        threads.append(threading.Thread(target=run,args=(str(i),)))
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()


def main():
    # 创建线程
    while True:
        global is_over
        is_over = False
        print("restart....")
        restart()


main()