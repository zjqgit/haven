# -*- coding: utf-8 -*-


from netkit.contrib.tcp_client import TcpClient
from reimp import Box

import time

client = TcpClient(Box, '127.0.0.1', 7777, timeout=5)
client.connect()

box = Box()
box.cmd = 101
box.body = '我爱你'

client.write(box)

t1 = time.time()

while True:
    # 阻塞
    box = client.read()
    print 'time past: ', time.time() - t1
    print box

    if client.closed():
        print 'server closed'
        break
