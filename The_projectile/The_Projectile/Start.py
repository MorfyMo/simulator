# import sys
# sys.path.append(r"/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages")
import graphics,Projectile
from graphics import *

class Start:
    def __init__(self,win):
        self.startBox=Rectangle(Point(780,78.25),Point(807,61.75))
        self.startBox.setFill("Red")
        self.start=Text(Point(793.5,70),"start")
        self.startBox.draw(win)
        self.start.draw(win)
    
    def click(self,p):
        # proj.clear()
        if(p!=None):
            return (780<=p.getX()<=807 and 61.75<=p.getY()<=78.25)
        return False

        