#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

sudo iptables -P OUTPUT ACCEPT
myhost = PingNetworkObj('http://www.google.fr')
print(myhost.isconnected)
"""
import subprocess

class PingNetworkObj(object):
    def __init__(self, host):
        self.host = host

    @property
    def host(self):
        return self.__host

    @host.setter
    def host(self, host):
        self.__host = host

    @property
    def isconnected(self):
        """Test network connection

        Args:
            func: decorated function
            timeout (int): timeout with a default value.

        Returns:
            link up: func(self, *args, **kwargs)
            link down: None

        """
        try:
            subprocess.run("ping -c 1 -w 1 " + self.__host, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return True
        except:
            return False
