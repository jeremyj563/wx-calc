#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from enum import Enum
class Operation(Enum):
    def __str__(self):
        if   self.value == 0: return '+'
        elif self.value == 1: return '-'
        elif self.value == 2: return '*'
        elif self.value == 3: return '/'
    ADD = 0
    SUBTRACT = 1
    MULTIPLY = 2
    DIVIDE = 3