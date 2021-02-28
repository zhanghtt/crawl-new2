#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import mitmproxy.http
from mitmproxy import ctx
import socket
import datetime
import _thread as thread

class Counter:
    def __init__(self):
        self.num = 0
        self.state = None
        thread.start_new_thread(self.receive_ation,(None,))

    def receive_ation(self,passsss):
        try:
            action_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            action_socket.bind(('0.0.0.0', 10053))
            action_socket.settimeout(100000)
            while True:
                (data, client_address) = action_socket.recvfrom(1024)
                print('change state from {} to {}'.format(self.state, data))
                if data == b'None':
                    self.state = None
                else:
                    self.state = data
        except KeyboardInterrupt:
            print('\rAction Server Shutdown!')
        finally:
            action_socket.close()

    def request(self, flow: mitmproxy.http.HTTPFlow):
        ctx.log.info("=============================")
        try:
            print('action {} Query for {} at {}'.format(self.state, flow.request.data.host,
                datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')))
        except Exception as e:
            print(e)
            print(flow.request.data.host)
            ctx.log.info("Error: %s" % flow.request)
            pass




addons = [
    Counter()
]