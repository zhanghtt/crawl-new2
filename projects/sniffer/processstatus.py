#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# !/usr/local/bin/python
# coding:utf-8
import psutil
import sys
import os


# 获取主机名称
def hostname():
    sys = os.name
    if sys == 'nt':
        hostname = os.getenv('computername')
        return hostname
    elif sys == 'posix':
        host = os.popen('echo $HOSTNAME')
        try:
            hostname = host.read()
            return hostname
        finally:
            host.close()
    else:
        return 'Unkwon hostname'


# 获取进程状态
def processStatus(processName):
    pids = psutil.pids()  # 获取主机所有的PID
    a = 1
    for pid in pids:  # 对所有PID进行循环
        p = psutil.Process(pid)  # 实例化进程对象
        if p.name() == processName:  # 判断实例进程名与输入的进程名是否一致（判断进程是否存活）
            print(a)  # 返回1，进程存活
            a += 1
    if a == 1:
        print(0)  # 返回0，进程逝去


# 获取进程PID
def processPID(processName):
    pids = psutil.pids()
    for pid in pids:
        p = psutil.Process(pid)
        if p.name() == processName:
            return pid
            return True  # 如果找到该进程则打印它的PID，返回true
    else:
        print('找不到进程' + processName)
        return False  # 没有找到该进程，返回false


# 获取进程的端口号
def processPort(pid):
    p = psutil.Process(pid)
    data = p.connections()
    print(data)
    data_listen = [x for x in data if 'LISTEN' in x]
    # pid_port=[]
    # for port in data_listen:
    #     pid_port.append((port.laddr.port))
    # return list(set(pid_port))
    return list(data_listen[0][3])[1]


hostname = hostname().strip()
#PID = processPID('nginx')
PID = processPID('Fiddler.exe')
port = processPort(PID)

json_data = [
    {"name": hostname + '-nginx', "port": port,  "PID": PID}
]

print(json_data)