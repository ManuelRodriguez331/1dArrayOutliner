import wx
from wx.lib.splitter import MultiSplitterWindow

class Panelleft(wx.Panel):
  def __init__(self, parent):
    wx.Panel.__init__(self, parent)
    self.text = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_MULTILINE, size=(100,800))
    sizer = wx.BoxSizer(wx.VERTICAL)
    sizer.Add(self.text, 0, wx.EXPAND, 0)
    self.SetSizer(sizer)

class Panelright(wx.Panel):
  def __init__(self, parent):
    wx.Panel.__init__(self, parent)
    self.text = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_MULTILINE, size=(300,800))
    sizer = wx.BoxSizer(wx.VERTICAL)
    sizer.Add(self.text, 0, wx.EXPAND, 0)
    self.SetSizer(sizer)


class MainFrame(wx.Frame):
  def __init__(self):
    wx.Frame.__init__(self, None, title="1dArrayOutliner")
    splitter = MultiSplitterWindow(self, style=wx.SP_LIVE_UPDATE)
    panel = Panelleft(splitter)
    splitter.AppendWindow(panel, sashPos=150)
    panel = Panelright(splitter)
    splitter.AppendWindow(panel)


if __name__ == "__main__":
    app = wx.App(False)
    frame = MainFrame()
    frame.Show()
    app.MainLoop()
