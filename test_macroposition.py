import keyboard as kb
import pyautogui as otog

#simple program that will display mouse coordinates if a certain keypress gets detected

def display():
    while True:
        pos = otog.position()
        once = kb.is_pressed('ctrl')
        if once:
            print("{0} dual   {1},{2} -- single mo".format(pos,pos[0]-1080,pos[1]))
            once = False
        if kb.is_pressed('esc'):
            break
display()