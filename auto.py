import pyautogui
import time
from pynput.keyboard import Key, Controller
import keyboard as kb  # pip install keyboard
import time

ctrl = Controller()
print("script [ON]")
while True:
    while kb.is_pressed('r'):
        while kb.is_pressed('4'):
            time.sleep(0.01)
            ctrl.press(Key.shift)
            pyautogui.click(707, 404)

            time.sleep(0.01)
            pyautogui.click(1308, 398)
            ctrl.release(Key.shift)
            time.sleep(0.01)
            
