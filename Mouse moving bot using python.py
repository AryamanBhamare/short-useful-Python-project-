# Mouse moving bot using python

import pyautogui as pag
# for pyautogi module just type " pip install pyautogui  " in the terminal section 

import random
import time

while True:
    x = random.randint(600,700)
    y = random.randint(200,600)
    pag.moveTo(x,y,0.5)
    time.sleep(2)
