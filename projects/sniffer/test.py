#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from scapy.all import *
import sys

def callback1(pkg):
    print(pkg.sprintf("%UDP.src.port%"))
    print(pkg.summary())
pkts = sniff(iface="Intel(R) Dual Band Wireless-AC 3165", filter="dst port 53", count=20, prn=callback1)
wrpcap("1.pcap", pkts)

