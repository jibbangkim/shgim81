
import time
import pywinmacro as pw

try:
    import pyperclip
    import pyautogui
except ModuleNotFoundError:
    import pip
    pip.main(['install', 'pyautogui'])
    pip.main(['install', 'pillow'])
    pip.main(['install', 'pyperclip'])
    pip.main(['install', 'opencv-python'])
    try:
        import pyperclip
        import pyautogui
    except ModuleNotFoundError:
        time.sleep(2)
        import pyperclip
        import pyautogui


def in_pivot():
    pw.key_on('alt')
    pw.key_on('n')
    pw.key_on('v')
    pw.key_on('t')
    pw.key_off('alt')
    pw.key_off('n')
    pw.key_off('v')
    pw.key_off('t')
    pw.key_press_once('tab')
    pw.key_press_once('down_arrow')
    pw.typing('Sheet1!$E$1')
    pw.key_press_once('enter')
    pw.key_on('alt')
    pw.key_on('j')
    pw.key_on('t')
    pw.key_on('s')
    pw.key_on('p')
    pw.key_off('alt')
    pw.key_off('j')
    pw.key_off('t')
    pw.key_off('s')
    pw.key_off('p')
    pw.key_press_once('tab')
    pw.key_press_once('enter')

def ctrl_shift_down():
    pw.key_on('control')
    pw.key_on('shift')
    pw.key_on('down_arrow')
    pw.key_off('control')
    pw.key_off('shift')
    pw.key_off('down_arrow')

def ctrl_alt_v():
    pw.key_on('control')
    pw.key_on('alt')
    pw.key_on('v')
    pw.key_off('control')
    pw.key_off('alt')
    pw.key_off('v')