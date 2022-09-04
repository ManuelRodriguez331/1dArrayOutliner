import wx

class Toolbar(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Toolbar, self).__init__(*args, **kwargs)
        self.img=wx.Bitmap('iconleft.png').ConvertToImage()
        self.graphics()
    def rotate90(self,number): # rotate 90 degree right
        tempimg=self.img
        for i in range(number):
          tempimg = tempimg.Rotate90()
        bmp = tempimg.ConvertToBitmap()
        return bmp
    def graphics(self):
        toolbar = self.CreateToolBar()
        #toolbar = self.CreateToolBar(style=wx.TB_TEXT | wx.TB_NOICONS)
        qtool2 = toolbar.AddTool(wx.ID_ANY, 'r', wx.Bitmap('iconleft.png'))

        qtool3 = toolbar.AddTool(wx.ID_ANY, 'r', self.rotate90(1))
        qtool4 = toolbar.AddTool(wx.ID_ANY, 'r', self.rotate90(3))
        qtool5 = toolbar.AddTool(wx.ID_ANY, 'r', self.rotate90(2))
        toolbar.Realize()
        self.Bind(wx.EVT_TOOL, self.OnQuit, qtool2)
        print("margin",toolbar.GetMargins(),toolbar.GetToolBitmapSize())

    def OnQuit(self, e):
        self.Close()


def main():
    app = wx.App()
    ex = Toolbar(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
