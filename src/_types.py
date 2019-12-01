#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from _enums import Operation

class Calculator():
    
    @property
    def value1(self):
        return self.__value1
    
    @value1.setter
    def value1(self, value1):
        self.__value1 = self.__to_float(value1)

    @property
    def value2(self):
        return self.__value2
    
    @value2.setter
    def value2(self, value2):
        self.__value2 = self.__to_float(value2)

    def __init__(self):
        self.result = 0
        self.display = ""
        self.operation = None

    def calc(self):
        self.operation = Operation(self.operation)
        try:
            if self.operation   == Operation.ADD:      self.result = self.value1 + self.value2
            elif self.operation == Operation.SUBTRACT: self.result = self.value1 - self.value2
            elif self.operation == Operation.MULTIPLY: self.result = self.value1 * self.value2
            elif self.operation == Operation.DIVIDE:   self.result = self.value1 / self.value2
            self.__set_display()
        except ZeroDivisionError:
            self.result = self.display = "Cannot divide by zero"
    
    def __set_display(self):
        self.display = f"{self.value1} {self.operation} {self.value2} = {self.result}"

    def __to_float(self, value):
        try: return float(value)
        except ValueError: return 0