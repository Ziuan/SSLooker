import sys
from time import sleep
import json
import os.path
import pytesseract
from PIL import Image
from PIL import ImageGrab
import win32gui
import win32ui
import win32con


env_filename = 'env.json'


def main(app_name):
    print('\n###  SSL  ###')
    wd = __file__.replace('main.py', '')
    os.chdir(wd)
    print('\n# CONFIG')
    if not os.path.isfile(env_filename):
        print('env.json missing. Copy env.json.example to env.json and fill in details')
        exit(0)

    with open(env_filename, 'r') as f:
        env = json.loads(f.read())

    save_path = env.get('save_path')
    if not os.path.exists(save_path):
        print('save_path incorrect in env.json. Was:'.ljust(40, ' ') + save_path)
        exit(0)
    else:
        print('Using screenshot path:'.ljust(40, ' ') + save_path)
    print('Taking screenshots for app:'.ljust(40, ' ') + app_name)

    possible_windows = _get_windows_bytitle(app_name, False)
    print(possible_windows)
    if len(possible_windows) is 0:
        print('No app with that name found')
        exit(0)

    for i in range(1):
        sleep(1)
        for window in possible_windows:
            screenshot(save_path, "img_" + str(window) + "_" + str(i), window)


def _get_windows_bytitle(title_text, exact=True):
    def _window_callback(hwnd, all_windows):
        all_windows.append((hwnd, win32gui.GetWindowText(hwnd)))
    windows = []
    win32gui.EnumWindows(_window_callback, windows)
    if exact:
        return [hwnd for hwnd, title in windows if title_text == title]
    else:
        return [hwnd for hwnd, title in windows if title_text in title]


def screenshot(save_path, filename, app=None):
    filepath = save_path + "\\" + filename
    if not app:
        app = win32gui.GetDesktopWindow()
    try:
        win32gui.SetForegroundWindow(app)
    except:
        pass
    bbox = win32gui.GetWindowRect(app)
    img = ImageGrab.grab(bbox)
    # img.save(filepath + ".jpeg", 'jpeg')
    # with Image.open(filepath + ".jpeg") as opened:
    text = pytesseract.image_to_string(img)
    tt = pytesseract.image_to_string(img, 'eng', '--oem 1')
    if ('demolished' in text):
        print('HIT1')
    if ('demolished' in tt):
        print('HIT2')
    return

    l, t, r, b = win32gui.GetWindowRect(app)
    h = b-t
    w = r-l
    hDC = win32gui.GetWindowDC(app)
    myDC = win32ui.CreateDCFromHandle(hDC)
    newDC = myDC.CreateCompatibleDC()

    myBitMap = win32ui.CreateBitmap()
    myBitMap.CreateCompatibleBitmap(myDC, w, h)

    newDC.SelectObject(myBitMap)

    sleep(.2)  # lame way to allow screen to draw before taking shot
    newDC.BitBlt((0, 0), (w, h), myDC, (0, 0), win32con.SRCCOPY)
    myBitMap.Paint(newDC)

    myBitMap.SaveBitmapFile(newDC, filepath + ".bmp")
    img = Image.open(filepath + ".bmp")
    new_img = img.resize((256, 256))
    new_img.save(filepath + ".jpeg", 'jpeg')


if __name__ == '__main__':
    if (len(sys.argv)) < 2:
        print('Application name missing')
        exit(0)

    main(sys.argv[1])
