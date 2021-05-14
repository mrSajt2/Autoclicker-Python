# Press f7 for start
# Press f8 for break
# mr_sajt author


import pyautogui as pg
import keyboard
while True:
    if keyboard.is_pressed('f7') == True:
        while True:
            pg.click()
            if keyboard.is_pressed('f8') == True:
                break