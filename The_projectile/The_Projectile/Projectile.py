# import sys
# sys.path.append(r"/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages")
import graphics
import math,HeightPic
from math import *
from graphics import *
from HeightPic import *

class Projectile:
    def __init__(self,angle,velocity,height):
        self.angleDegree=float(angle)
        self.angle=radians(float(angle))
        self.velocity=velocity
        self.x=0.0
        self.initial=0.0
        self.height=float(height)
        self.y=float(height)
        self.time=0
        self.shape=Oval(Point(54,324-(self.height+2)),Point(65,324-(self.height+2+324)))
        # self.shape.draw(win)
    
    def update(self,time,win):
        if(float(self.y)>0 or float(self.x)==0):
            self.time+=float(time)
            x=float(self.velocity)*cos(float(self.angle))*float(self.time)
            y=float(self.height)+(float(self.velocity)*sin(float(self.angle))*float(self.time)-4.9*pow(float(self.time),2))             
            self.shape.undraw()
            """for the version including draw point onto the window""" 
            #self.shape.move(x-float(self.x),y-float(self.y))
            self.shape.move(x-float(self.x),float(self.y)-y)
            self.shape.draw(win)
            self.x=x
            self.y=y
    
    def getX(self):
        return self.x 
    
    def getY(self):
        return self.y
    
    def setVelocity(self,v):
        self.velocity=float(v)
    
    #set initial angle
    def setAngle(self,a):
        self.angleDegree=float(a)
        self.angle=radians(float(a))
    
    #clear the projectile item on graph and draw a renewed version of projectile
    def setY(self,win,h):
        # self.shape.undraw()
        self.clear()
        self.height=h
        self.y=h
        # self.shape.draw(Oval(Point(5+self.x,self.y+2),Point(15+self.x,self.y+2)))
          
    #set the initial x position
    def setX(self,win,n):
        self.initial=n
        self.x=n
        self.time=0
    
    # def inputValue(self):
    #     a=float(input("The initial angle(°):"))
    #     v=float(input("The initial velocity(m/s):"))
    #     h=float(input("The initial height(m):"))
    #     t=float(input("The time for check(s):"))
    #     return a,v,h,t
    
    """def adjAngle(self,direc):
        # arrow=Line(P1,P2)
        # getKey()
        if(direc>0):
            self.angleDegree+=1
        elif(direc<0):
            self.angleDegree-=1
        self.angle=radians(self.angleDegree)"""
    
    # draw angle on graph 
    def projection(self,win):
        self.arrow=Line(Point(60+float(self.x),735),Point(70+cos(float(self.angle))*100,735-sin(float(self.angle))*100))
        self.arrow.setArrow("last")
        self.arrow.setWidth(2)
        self.arrow.draw(win)
        # return arrow
    
    # tag the distance on the axis near the bottom of the graph
    def length(self,win):
        index=0
        for i in range(61,980,42):
            tag=Line(Point(i,735),Point(i,730))
            label=Text(Point(i,750),round(index,4))
            index+=42.3
            tag.setWidth(2)
            tag.draw(win)
            label.draw(win)
    
    # update angle
    def updateAngle(self,win,angle):
        self.arrow.undraw()
        # arrow=Line(Point(60+float(self.x),324),Point(70+cos(radians(float(angle)))*100,324-sin(radians(float(angle)))*100))
        self.arrow=Line(Point(61,735),Point(61+cos(radians(float(angle)))*100,735-sin(radians(float(angle)))*100))
        self.arrow.setArrow("last")
        self.arrow.setWidth(2)
        self.arrow.draw(win)
    
    def getAngle(self):
        return self.angleDegree
    
    def clear(self):
        move_distance=self.x
        move_height=self.y
        self.x=0.0
        self.height=self.y=HeightPic.getH(self)
        self.time=0.0
        self.shape.move(-move_distance,move_height)
        
        
    
    def drawP(self,win):
        self.shape=Oval(Point((55+float(self.x)),(735-(float(self.y)+2))),Point((65+float(self.x)),(735-(float(self.y)+10))))
        self.shape.setFill("Red")
        self.shape.draw(win)