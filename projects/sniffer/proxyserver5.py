#!/usr/bin/env python3
# coding=utf-8
import socket
import select
import logging
import os
import re
import time

import chardet

logsDir = "logs"
if not os.path.isdir(logsDir):
    os.mkdir(logsDir)

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='logs/logs.log',
                    filemode='a')

# C的IP和端口
to_addr = ('0.0.0.0', 8889)

def getAddr(d):
 a = re.search("Host: (.*)\r\n", d)
 host = a.group(1)
 a = host.split(":")
 if len(a) == 1:
  return (a[0], 80)
 else:
  return (a[0], int(a[1]))


class Proxy:
    def __init__(self, addr):
        self.proxy = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.proxy.bind(addr)
        self.proxy.listen(10)
        self.inputs = [self.proxy]
        self.route = {}

    def serve_forever(self):
        logging.info('proxy listen...')
        while 1:
            readable, _, _ = select.select(self.inputs, [], [])
            for self.sock in readable:
                if self.sock == self.proxy:
                    self.on_join()
                else:
                    try:
                        data = self.sock.recv(8192)
                    except Exception as e:
                        logging.error(str(e))
                        self.on_quit()
                        continue

                    if not data:
                        self.on_quit()
                    else:
                        try:
                            self.route[self.sock].send(data)
                        except Exception as e:
                            logging.error(str(e))
                            self.on_quit()
                            continue

    def on_join(self):
        client, addr = self.proxy.accept()
        logging.info("proxy client " + str(addr) + 'connect')
        data = client.recv(4096)
        if data:
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
            self.inputs.append(sock)
            if method == "CONNECT":
                start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
                self.sock.sendall(bytes(
                    "HTTP/1.1 200 Connection Established\r\nFiddlerGateway: Direct\r\nStartTime: {0}\r\nConnection: close\r\n\r\n".format(
                        start_time), charset))
            else:
                forward = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                addr = getAddr(data.decode(charset))
                forward.connect(addr)
                self.inputs += [client, forward]
                self.route[client] = forward
                self.route[forward] = client

        # 删除连接

    def on_quit(self):
        ls = [self.sock]
        if self.sock in self.route:
            ls.append(self.route[self.sock])
        for s in ls:
            if s in self.inputs:
                self.inputs.remove(s)
            if s in self.route:
                del self.route[s]
            s.close()


if __name__ == "__main__":
    try:
        Proxy(('', 8888)).serve_forever()
    except KeyboardInterrupt:
        logging.error("KeyboardInterrupt")