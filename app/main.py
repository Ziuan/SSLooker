import sys
import time
import json
import os.path
import pytesseract
from PIL import Image
import win32gui

env_filename = 'env.json'


def main(app_name):
    print('\n###  SSL  ###')
    wd = __file__.replace('main.py', '')
    print('Setting WD'.ljust(40, ' ') + wd)
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

    for i in range(10):
        time.sleep(1)


def _get_windows_bytitle(title_text, exact=False):
    def _window_callback(hwnd, all_windows):
        all_windows.append((hwnd, win32gui.GetWindowText(hwnd)))
    windows = []
    win32gui.EnumWindows(_window_callback, windows)
    if exact:
        return [hwnd for hwnd, title in windows if title_text == title]
    else:
        return [hwnd for hwnd, title in windows if title_text in title]


if __name__ == '__main__':
    if (len(sys.argv)) < 2:
        print('Application name missing')
        exit(0)

    main(sys.argv[1])
