import pywinmacro as pw
import pywinmacro2 as pw2
import pyautogui
import time

pw.double_click(pw.find_on_screen('button_b.PNG',confidence=0.7))
pw2.in_pivot()

pw.key_on('control')
pyautogui.hotkey('ctrl', 'shift', 'down')
pyautogui.hotkey('shift', 'up')
pyautogui.hotkey('shift', 'up')
pyautogui.hotkey('shift', 'up')
pyautogui.hotkey('ctrl', 'shift', 'down')
pyautogui.hotkey('ctrl', 'shift', 'up')
pyautogui.hotkey('ctrl', 'shift', 'down')
pyautogui.hotkey('ctrl', 'shift', 'up')

# pw2.ctrl_shift_down()


# pw.key_on('shift')
# pw.key_press_once('up_arrow')
# pw.key_on('shift')
# pw.key_press_once('up_arrow')
# pw.key_on('shift')
# pw.key_press_once('up_arrow')
# pw.key_press_once('up_arrow')
# pw.key_press_once('up_arrow')
# pw.key_off('shift')
#
#
# pw.ctrl_c()
# pw.key_press_once('right_arrow')
# pw.key_press_once('right_arrow')
# pw.key_press_once('right_arrow')
#
# pw2.ctrl_alt_v()
# pw.key_press_once('down_arrow')
# pw.key_press_once('down_arrow')
# pw.key_press_once('tab')
# pw.key_press_once('tab')
# pw.key_press_once('right_arrow')
# pw.key_press_once('spacebar')
# pw.key_press_once('enter')
