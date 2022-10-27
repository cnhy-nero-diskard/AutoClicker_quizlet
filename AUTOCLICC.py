
import pyautogui
import pyperclip
import pymsgbox as msg
import time
import logging
import sys
import keyboard

"""
1. Will only work with 2 monitors(testing grounds on 2ndary) because im too lazy. So feel free to fork if you want
2. I am lazy asf
3. Holabels

Dependencies:
1. Opera GX (it has a built-in save as PDF)
2. Quizlet bypasser extension(located somewhere in github)
    2.1 This extension won't work right away. It will need multiple reloads 
    2.2 Hence, why this program existed in the first place.
    2.3 For some reason, when I manually reload the page, it never manages to get unlocked
    2.4 The bot only needed some 4 retries and its good to go
3. Despite my laziness, I will update this in the near future. It's just calculus kicking
   my ass that's all
    3.1 Hopefully, I will either go back to reviewing my stock BS4 knowledge or finally learn how to use PIL
    3.2 Tip: Open quizlet in incognito as this multiple reloads in the normal tab and the cookies will accumulate

4. This program can only exit itself when pyautogui.FAILSAFEexception gets triggered

5.Issues/Quirks:
    1.This program doesn't know if the webpage is at the next chapter (no plans)
    2.The program will never overwrite a file with the same name. So it might help us with 5.1
    3. A program dedicated to renaming the pdf files is not in planning
"""

"""Class implementation Ideas:
        1. Monitor number(1 if left monitor, 2 if right monitor)
        2. Internet speed tied to time.sleep()
        3. Activate or deactivate the debugger
        4. The zoom size of the browser (the current setting is at 110%)
        5. Hopefully make the program flexible by making the keymaps as customizable as possible through some override

        """

FORMAT = ("%(asctime)s  %(name)s  %(levelname)s  %(message)s")

logger = logging.getLogger("AUTOCLICKER")
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter(FORMAT)

console = logging.StreamHandler(sys.stdout)
console.setFormatter(formatter)
logger.addHandler(console)

file_handler = logging.FileHandler('autog.log', mode='a')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def ctrl(keystroke): #a four-liner macro key with ctrl
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown(keystroke)
    pyautogui.keyUp(keystroke)
    pyautogui.keyUp('ctrl')
def isexited(): #unused atm: an exception occurs whenever I use this in my code
    if keyboard.is_pressed('esc'):
        logger.warning("Script terminated by keypress")
        raise Exception("User has terminated the script")

        
    
   
 
def contains(keywords, text):
    for i in keywords:
            if text.__contains__(i):
                print(text)
                return False
    return True
def clik():
    coord = (2710,825),(2710,775)
    scrate = 5000
    pyautogui.scroll(-scrate)
    pyautogui.moveTo(coord[0][0],coord[0][1])
    pyautogui.click()
    pyautogui.moveTo(coord[1][0],coord[1][1])
    pyautogui.click()
    return coord


def moveandclick():
    keywords = ["soluzioni", "limite", "limit", "raggiunto","Upgrade"] #some keywords that might be present in the pop up paywall
    scroll_mag = 20000
    coords = {'save':((3578,260),(3620,517)),
               'drag':((2325, 535), (2541,593)),
                 }
    save = (3578,260),(3620,517)
    drag = [(2325, 535), (2541,593)]
    t_clickcoord = (2483,574),(2561,599)


    iscleared = False
    iter = 0 #will keep an iterator for later analysis
    print("bahog")
    try:
        while True:
            isexited()
            while not iscleared:
                isexited()
                pyautogui.moveTo(drag[0])
                pyautogui.click()
                #pyautogui.dragTo(2561,599,0.35,button='left')

                pyautogui.doubleClick(t_clickcoord[0]) #effectively replaces dragTo()
                pyautogui.click()
                ctrl('c')
                text = pyperclip.paste()
                iscleared = contains(keywords,text)
                if not iscleared:
                    iter += 1
                    ctrl('r')
                    time.sleep(4)
                    pyautogui.click()
                    logger.info("keyword detected: {}".format(text))
                    logger.info("Reload number: {}".format(iter))
            iter = 0    
            clik()
            pyautogui.click()
            pyautogui.moveTo(save[0]) #move to a usually vacant spot on the webpage area
            pyautogui.rightClick()    
            pyautogui.click(save[1])         #click on "Save as PDF"
            time.sleep(0.5)           #wait for the popup screen on top-left
            ctrl('c')
            logger.info("Saved pdf file: {}".format(pyperclip.paste()))
            pyautogui.click(2724,569) #confirm save
            isexited()
            time.sleep(1)
            pyautogui.scroll(-scroll_mag)
            time.sleep(2)
            pyautogui.click(3100,835) #the position of "exercise x
            pyautogui.scroll(scroll_mag) #scroll back to top
            time.sleep(2)
            logger.debug('[SUCCESSFUL] Next Webpage loading...')
            isexited()

            iscleared = False

    except pyautogui.FailSafeException:
        logger.warning("User has force hovered over (0,0). Stopping script")    
        

if __name__ == "__main__":
    moveandclick()
