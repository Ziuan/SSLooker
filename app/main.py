import sys
import time
import json
import os.path

env_filename = 'env.json'


def main(app_name):
    print('\n###  SSL  ###\n')
    if not os.path.isfile(env_filename):
        print('env.json missing. Copy env.json.example to env.json and fill in details')
        exit(0)

    with open(env_filename, 'r') as f:
        env = json.loads(f.read())

    print('# CONFIG')
    save_path = env.get('save_path')
    if not os.path.exists(save_path):
        print('save_path incorrect in env.json. Was:       ' + save_path)
        exit(0)
    else:
        print('Using screenshot path:                      ' + save_path)

    print('Taking screenshots for app:                 ' + app_name)
    # for i in range(10):
    #     time.sleep(1)
    #     print(i)


def _get_windows_bytitle(title_text, exact=False):
    import win32gui

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
