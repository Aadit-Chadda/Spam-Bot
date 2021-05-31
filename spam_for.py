import time
import keyboard
import pyautogui

repeat = int(input("repetition: "))
time.sleep(10)
for i in range(repeat + 1):
    if keyboard.is_pressed('e'):
        break
    text = (str(i) + ". Hello World")
    pyautogui.typewrite(text)
    pyautogui.press("enter")

print('Spam Accomplished')
