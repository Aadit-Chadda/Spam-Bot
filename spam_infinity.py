import time
import keyboard
import pyautogui

time.sleep(30)
while True:
    if keyboard.is_pressed('e'):
        break
    pyautogui.typewrite("Hello Infinity")
    pyautogui.press("enter")
