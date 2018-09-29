import wx


class MyFrame(wx.Frame):  # 创建自定义Frame
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=-1, title="Hello World", size=(300, 300))  # 设置窗体

        """
        panel和sizer是wxpython提供的窗口部件。是容器部件，可以用于存放其他窗口部件
        """
        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)
        panel.SetSizer(sizer)

        txt = wx.StaticText(panel, -1, "Hello World!")  # 创建静态文本组件
        sizer.Add(txt, 0, wx.TOP | wx.LEFT, 100)

        self.Center()  # 将窗口放在桌面环境的中间


app = wx.App()

"""
Every wx application must have a single ``wx.App`` instance, and all
    creation of UI objects should be delayed until after the ``wx.App`` object
    has been created in order to ensure that the gui platform and wxWidgets
    have been fully initialized.
"""

frame = MyFrame(None)  # 为顶级窗口
frame.Show(True)

app.MainLoop()
