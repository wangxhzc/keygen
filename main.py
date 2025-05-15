import wx
import wx.xrc
import KeygenUi

def main():

    # Next, create an application object.
    app = wx.App()

    # Then a frame.
    frm = KeygenUi.MainFrame(None)

    # Show it.
    frm.Show()

    # Start the event loop.
    app.MainLoop()

if __name__ == "__main__":
    main()
