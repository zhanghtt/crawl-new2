#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# encoding:utf-8
import socket
import _thread as thread
import re
import time
import traceback

import chardet


def getAddr(d):
 a = re.search("Host: (.*)\r\n", d)
 host = a.group(1)
 a = host.split(":")
 if len(a) == 1:
  return (a[0], 80)
 else:
  return (a[0], int(a[1]))

def client(conn, caddr):
    remote_socket = 0
    while 1:
        try:
            data = conn.recv(40960)
            if remote_socket is 0:
                # 拆分头信息
                charset = chardet.detect(data)["encoding"]
                host_url = data.decode(charset).split("\r\n")[0].split(" ")
                method, host_addr, protocol = map(lambda x: x.strip(), host_url)
                # 如果 CONNECT 代理方式
                if method == "CONNECT":
                    host, port = host_addr.split(":")
                else:
                    host_addr = data.decode(charset).split("\r\n")[1].split(":")
                    # 如果未指定端口则为默认 80
                    if 2 == len(host_addr):
                        host_addr.append("80")
                    name, host, port = map(lambda x: x.strip(), host_addr)
                    # 建立 socket tcp 连接
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.connect((host, int(port)))
                remote_socket = sock
                if method == "CONNECT":
                    start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
                    sock.sendall(bytes(
                        "HTTP/1.1 200 Connection Established\r\nFiddlerGateway: Direct\r\nStartTime: {0}\r\nConnection: close\r\n\r\n".format(
                            start_time), charset))
                    continue
            if data:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                addr = getAddr(data.decode("utf8"))
                print("目的服务器：", addr)
                s.connect(addr)
                print('发给目的服务器数据：',data)
                s.sendall(data)#将请求数据发给目的服务器
                d = s.recv(40960)#接收目的服务器发过来的数据
                s.close()#断开与目的服务器的连接
                print('接收目的服务器数据:',d)
                conn.sendall(d)#发送给代理的客户端
        except Exception as e:
            import sys
            print(data,(host, int(port)),file=sys.stderr)
            print('代理的客户端异常：%s, ERROR:%s'%(caddr,e),file=sys.stderr)
            traceback.print_exc()
            conn.close()
            break

def serve(PORT = 8888):
 # 创建
 IP = "0.0.0.0"
 s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 s.bind((IP, PORT))
 s.listen(10)
 print('proxy start...')
 while True:
  conn, addr = s.accept()
  # print('conn:', conn)
  # print("addr:", addr)
  thread.start_new_thread(client, (conn, addr))

try:
 serve()
except Exception as e:
 print('代理服务器异常',e)

print('server end!!!')