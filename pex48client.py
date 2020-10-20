#!/usr/bin/env python

import socket

class pex48client(object):
    def __init__(self,ip_addr,port):
        self._ip_addr = ip_addr
        self._port = port
        return

    def _send_cmd(self,cmd):
        data = b'\x00'
        while(data!=b'A'):
            sock = socket.socket()
            sock.settimeout(2.0)
            sock.connect((self._ip_addr, self._port))
            sock.send(cmd+b'\n',2)
            try:
                data = sock.recv(1)
            except:
               continue
            sock.close()
            
        return

    def stop(self):
        self._send_cmd(b'q')
        return

    def start(self):
        self._send_cmd(b's')
        return

    def read(self):
        retval = -1
        while(retval == -1):
            sock = socket.socket()
            sock.settimeout(2.0)
            sock.connect((self._ip_addr, self._port))
            sock.send(b'r\n',2)
            try:
                data = sock.recv(8)
            except:
               #print("Timeout!")
               continue
           
            retval = int.from_bytes(data,"little")
            sock.close()
        return retval

# EOF

