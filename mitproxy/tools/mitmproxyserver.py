#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from mitmproxy import proxy, options
from mitmproxy.tools.web.master import WebMaster
from mitmproxy.tools.dump import DumpMaster
import threading,asyncio

from mitproxy.addons import addon, tls_passthrough1


class MitmWebWraper(object):
    mitmweb = None
    thread = None

    def loop_in_thread(self, loop, mitmweb):
        asyncio.set_event_loop(loop)
        mitmweb.run()

    def start(self):
        opts = options.Options(listen_host='0.0.0.0', listen_port=8080)
        pconf = proxy.config.ProxyConfig(opts)
        self.mitmweb = DumpMaster(opts)
        self.mitmweb.server = proxy.server.ProxyServer(pconf)
        self.mitmweb.addons.add(addon)
        self.mitmweb.addons.add(tls_passthrough1)
        loop = asyncio.get_event_loop()
        self.thread = threading.Thread(
            target=self.loop_in_thread, args=(loop, self.mitmweb))

        try:
            self.thread.start()
        except KeyboardInterrupt:
            self.mitmweb.shutdown()


if __name__ == "__main__":
    mitmweb_wraper = MitmWebWraper()
    mitmweb_wraper.start()