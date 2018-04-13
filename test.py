#!/usr/bin/env python3
"""
-*- coding: utf-8 -*-
This script is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 3 of the License, or (at your option) any later version.

This script is provided in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
"""


class MembersObj(object):
    def __init__(self):
        self.__members = dict()
    def __repr__(self):
        print("repr member")
        return str(self.__members)
    def __str__(self):
        print("str member")
        return repr(self)
    def __setitem__(self, index, value):
        self.__members[index]=value
    def __getitem__(self, index):
        return self.__members[index]
    def __len__(self):
        return len(self.__members)
    def sortkeys(self):
        return sorted(self.__members)
    def items(self):
        return self.__members

class PythonObj(object):
    def __init__(self, inspect_object):
        self.__inspect_object=inspect_object
        self.__name=""
        self.__docstring=""
        self.__level=0
        self.members = MembersObj()
    def __repr__(self):
        print("str obj")
        return str(self.__inspect_object)+" toto"
    def __str__(self):
        return repr(self)

    def getallstr(self, member=None):
        if member is None:
            member=self

        output = str(member)
        for idmember in member.members.sortkeys():
            output += self.getallstr(member.members[idmember])

        return output

class ModuleObj(PythonObj):
    def __init__(self, inspect_object):
        PythonObj.__init__(self, inspect_object)




obj=dict()
obj["mon objet"]="mon inspect"
a=ModuleObj(obj)
member=dict()
member["Mon membre"]="zekjfzhe"
#85784
obj2=dict()
obj2["mon objet2"]="mon inspect2"
a.members["obj2"]=PythonObj(obj2)
obj3=dict()
obj3["mon objet3"]="mon inspect3"
a.members["obj3"]=PythonObj(obj3)
obj4=dict()
obj4["mon objet4"]="mon inspect4"
b=PythonObj(obj4)
(a.members["obj2"]).members["objet 4"]=b


print(a.getallstr())


#print(a)
#print(a.members)
#print((a.members["obj2"]).members["objet 4"])

