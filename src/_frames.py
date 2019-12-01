#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import wx, gettext, abc
from _base_frames import BaseFrame

class MainFrame(BaseFrame):
    def __init__(self, calculator, *args, **kwds):
        BaseFrame.__init__(self, *args, **kwds)
        self.__calculator = calculator

    def button_execute_onclick(self, e):
        self.__set_calculator()
        self.__calculator.calc()
        self.__show_result()
        self.__log_result()
        e.Skip()
    
    def button_reset_onclick(self, e):
        self.__clear_form()
        e.Skip()

    def __set_calculator(self):
        self.__calculator.operation = self.radiobox_operator.GetSelection()
        self.__calculator.value1 = self.text_value1.GetValue()
        self.__calculator.value2 = self.text_value2.GetValue()
    
    def __show_result(self):
        text = f"{self.__calculator.result}\n"
        self.text_result.AppendText(text)

    def __log_result(self):
        text = f"{self.__calculator.display}\n"
        self.text_log.AppendText(text)
    
    def __clear_form(self):
        self.text_value1.Clear()
        self.text_value2.Clear()
        self.text_result.Clear()