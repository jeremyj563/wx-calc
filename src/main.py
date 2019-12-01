#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import wx, gettext
from _frames import BaseFrame, MainFrame
from _types import Calculator

class App(wx.App):
    def OnInit(self):
        self.frame = MainFrame(Calculator(), None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

if __name__ == "__main__":
    gettext.install("frame") # replace with the appropriate catalog name
    app = App(0)
    app.MainLoop()