# import sys
# sys.path.append(r"/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages")
import graphics
from graphics import *

class HeightPic:
    def __init__(self,height):
        if(float(height)>0):
            self.height=height
        else:
            self.height=0
        self.width=20
    
    def getH(self):
        return self.height
    
    def drawH(self,win):
        platform=Rectangle(Point(50,734),Point(70,(734-self.height)))
        platform.setFill("white")
        platform.draw(win)
        
    def setH(self,win,h):
        self.height=h