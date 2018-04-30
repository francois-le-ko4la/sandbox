#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    calc_limit(60, 20, i)

test = CalcLimit(60,20)
for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    test.current_id = i
    print("{} - {}".format(test.row, test.column))

"""
import numbers

def calc_limit(stripe_size, element_size, current_id):

    ratio = int(stripe_size/element_size)
    print("nmbr elem / stripe: {}".format(ratio))

    row = int(current_id/ratio)
    
    column = current_id - (row * ratio)
    print(row, column)


class CalcLimit(object):
    def __init__(self, stripe_size, element_size):
        self.current_id = 0
        self.stripe_size = stripe_size
        self.element_size = element_size

    @property
    def stripe_size(self):
        return self.__stripe_size

    @stripe_size.setter
    def stripe_size(self, value):
        if isinstance(value, numbers.Integral) and value > 0:
            self.__stripe_size = value
        else:
            raise TypeError("invalid stripe_size")

    @property
    def element_size(self):
        return self.__element_size

    @element_size.setter
    def element_size(self, value):
        if isinstance(value, numbers.Integral) and value > 0:
            self.__element_size = value
        else:
            raise TypeError("invalid element_size")

    @property
    def ratio(self):
        return int(self.__stripe_size/self.__element_size)

    @property
    def current_id(self):
        return self.__current_id

    @current_id.setter
    def current_id(self, value):
        if isinstance(value, numbers.Integral):
            self.__current_id = value
        else:
            raise TypeError("invalid current_id")

    @property
    def row(self):
        return int(self.__current_id/self.ratio)

    @property
    def column(self):
        return self.__current_id - (self.row * self.ratio)
