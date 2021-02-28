#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket
import thread
import re
import traceback
import sys
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
    while 1:
        try:
            data = conn.recv(409600)
            if data:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                charset = chardet.detect(data)["encoding"]
                if charset:
                    addr = getAddr(data.decode(charset))
                else:
                    addr = getAddr(data.decode())
                print("目的服务器：", addr)
                s.connect(addr)
                #print('发给目的服务器数据：', data.decode(charset))
                s.sendall(data)#将请求数据发给目的服务器
                d = s.recv(409600)#接收目的服务器发过来的数据
                s.close()#断开与目的服务器的连接
                # charset1 = chardet.detect(d)["encoding"]
                # if charset1:
                #     print('接收目的服务器数据:',d.decode(charset1))
                # else:
                #     print('接收目的服务器数据:', d.decode('utf8'))
                conn.sendall(d)#发送给代理的客户端
        except Exception , e:
            print('代理的客户端异常：%s, ERROR:%s'%(caddr, e), data)
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