import pyautogui
import time
from pynput.keyboard import Key, Controller
import keyboard as kb  # pip install keyboard
import time

ctrl = Controller()

while True:
    x, y = pyautogui.position()
    print("script [OFF]     ",x,y, end="\r")
    while kb.is_pressed('r'):

        time.sleep(0.001)
        ctrl.press(Key.shift)
        pyautogui.click(707, 404)

        time.sleep(0.001)
        pyautogui.click(1308, 398)
        ctrl.release(Key.shift)
        time.sleep(0.001)


        x, y = pyautogui.position()
        print("script [ON]      ",x,y, end="\r")

