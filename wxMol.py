#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2010 Hubert Hanghofer
# hubert.hanghofer.net
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import locale, wx
from molcalc import parse_formula
from wxMolGui import wxMolFrame

class wxAppFrame(wxMolFrame):
    def __init__(self, *args, **kwds):
        wxMolFrame.__init__(self, *args, **kwds)
        locale.setlocale(locale.LC_ALL, '')
        self.dp = locale.localeconv()["decimal_point"]
        self.Bind(wx.EVT_SET_FOCUS, self.on_focus, self.txtOutput)
        
    def on_enter(self, event):
        try:
            p = parse_formula(str(self.txtInput.GetValue()))
            self.txtStatus.ChangeValue(p)
            r = str(eval(p))
            if self.dp != '.':
                t = r.partition('.')
                r = t[0] + self.dp + t[2]
            self.txtOutput.ChangeValue(r)
        except (NameError, SyntaxError, UnicodeEncodeError,
                ZeroDivisionError) as detail:
            self.txtOutput.ChangeValue(repr(detail))
            
    def on_copy(self, event):
        self.txtOutput.SetSelection(-1, -1)
        self.txtOutput.Copy()
    
    def on_focus(self, event):
        self.txtOutput.SetSelection(-1, -1)

if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    frame_1 = wxAppFrame(None, wx.ID_ANY, "")
    app.SetTopWindow(frame_1)
    frame_1.Show()
    app.MainLoop()
