def screenshot(hwnd=None):
    import win32gui
    import win32ui
    import win32con
    from time import sleep
    if not hwnd:
        hwnd = win32gui.GetDesktopWindow()
    l, t, r, b = win32gui.GetWindowRect(hwnd)
    h = b-t
    w = r-l
    hDC = win32gui.GetWindowDC(hwnd)
    myDC = win32ui.CreateDCFromHandle(hDC)
    newDC = myDC.CreateCompatibleDC()

    myBitMap = win32ui.CreateBitmap()
    myBitMap.CreateCompatibleBitmap(myDC, w, h)

    newDC.SelectObject(myBitMap)

    win32gui.SetForegroundWindow(hwnd)
    sleep(.2)  # lame way to allow screen to draw before taking shot
    newDC.BitBlt((0, 0), (w, h), myDC, (0, 0), win32con.SRCCOPY)
    myBitMap.Paint(newDC)
    myBitMap.SaveBitmapFile(newDC, 'c:\\tmp.bmp')
