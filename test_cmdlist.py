""" from turtle import shape
import pyautogui

#will draw a square at monitor


class macro:
    def __init__(self) -> None:
        self.size = 800 #pixel size
        self.shape = shape
        self.origin = origin #must be a tuple of tuples or list of paired lists
        self.tv = 'main' # main-> +(0,0) secondary-> +(1920,1080)

    def isshape(self,shape) -> int:
        if shape == "square":
            return 0
        return 0
    def monito(type):
        if type == 'main':
            return (0,0)
        elif type == 'secondary':
            return (1920,1080)
        
    def coords(self,o,monitor = 'main'):
        displ = monito(self,monitor)
        coords = [(o),(o+)
    def drawshape(self,coordlist,type = 0) -> None:
        pyautogui.moveTo(coordlist[0])
        for drag in coordlist:
            pyautogui.dragTo(drag,button='left')
def __main__():
    mac = macro()
    print(mac.size)
    print(mac.shape)

if __name__ == "__main__":
    __main__()
 """