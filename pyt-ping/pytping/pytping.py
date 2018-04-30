#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from curse import *
from ping import *
from configyaml import *
from members import *
from threading import Timer


class HostObject(object):
    def __init__(self, label, host, port=False):
        self.__started = True
        self.isconnected = False
        self.label = label
        self.host = host
        self.__ping = PingNetworkObj(host)
        self.__port = port
        self.__refresh()

    @property
    def isconnected(self):
        return self.__isconnected

    @isconnected.setter
    def isconnected(self, value):
        self.__isconnected = value

    def __refresh(self):
        if self.__started is not True:
            return
        self.isconnected = self.__ping.isconnected
        #print("{} - {}\n".format(self.label,self.isconnected))
        self.__timer = Timer(2, self.__refresh)
        self.__timer.start()

    def stop(self):
        self.__started = False
        #self.__timer.cancel()


class PythonPing(object):
    def __init__(self):
        self.__yaml = ConfigYAML("./config.yml")
        self.__config = self.__yaml.config
        self.__host_list = MembersObj()
        for label in self.__config:
            self.__host_list.append(HostObject(label, self.__config[label]['host']))
        self.__screen = ScreenCurses(self.__host_list)

    def run(self):
        """ start screen """
        self.__screen.run()
        """ EXIT """
        for host in self.__host_list:
            host.stop()

a = PythonPing()
a.run()

