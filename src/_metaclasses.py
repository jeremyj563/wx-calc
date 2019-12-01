#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import wx, abc
class FrameABCMeta(abc.ABCMeta, type(wx.Frame)): 
    pass