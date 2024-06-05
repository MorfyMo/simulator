# import sys
# sys.path.append(r"/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages")
import Projectile,Start,HeightPic
import time
import graphics
from graphics import *
from Start import *
from Projectile import *
from HeightPic import *

def main():
    reminder()
    
    #initialize static objects,including the window,tags,and graphics
    win=GraphWin("projection lab",1100,800)
    win.setBackground("white") 
    a,v,h=text(win)   
    button,platform,projec=static(win)
    projec.projection(win)
    
    while(True):
        graph(win,a,v,h,button,platform,projec)
    # theta=float(input("inital angle between ground and bomb:"))
    # vi=float(input("initial velocity of the bomb(m/s):"))
    # hi=float(input("initial height of the bomb(m):"))
    
def reminder():
    print("\nReminder on the program side:")
    print("provide a platform for entering any value\n for simulating corresponding passing distance horizontally")
    print("the following is the program")
    print("------------------------------------------")

#the window 
def graph(win,a,v,h,button,platform,proj):
    proj.clear()
    output=Text(Point(700,70),"")
    output.draw(win)
            
    while(True):
        
        # the time intervel when the angle, velocity, height can be altered
        clik=button.click(win.checkMouse())
        key=win.checkKey()
        while(not clik):
            # angleText=float(a.getText())
            key=win.checkKey()
            if(key=="Up"):
                a.setText(float(a.getText())+1)
                proj.updateAngle(win,float(a.getText()))
            elif(key=="Down"):
                a.setText(float(a.getText())-1)
                proj.updateAngle(win,float(a.getText())) 
            elif(key==""):               
                p=win.checkMouse()
                if(p!=None):
                    clik=button.click(p)
        
        #the moment when the projectile start 
        if(clik or key=="Space"):
            output.setText("")
            theta,velocity,height=entry(a,v,h)
            platform.setH(win,height)
            proj.setY(win,height)
            proj.setX(win,0)
            proj.setAngle(theta)
            proj.updateAngle(win,theta)
            proj.setVelocity(velocity)
                                    
            #show the motion track of the projectile
            while(float(proj.getY())>=0.0):
                proj.update(0.2,win)
                time.sleep(0.1)
                # proj.drawP(win)
                update(30)
                
            output.setText(round(proj.getX(),4))

"""#draw the projection arrow on the graph according to the given angle
def projection(angle):
    arrow=Line(Point(58,324),Point(70+cos(radians(float(angle)))*100,324-sin(radians(float(angle)))*100))
    arrow.setArrow("last")
    arrow.setWidth(3)
    # arrow.draw(win)
    return arrow"""

#initialize tags and entries
def text(win):
    #initialize theta text
    theta=Text(Point(41.55,70),"θ(°)")
    thetaEntry=Entry(Point(110.8,70),4)
    thetaEntry.setText(45)
    
    #initialize velocity text
    velocity=Text(Point(207.88,70),"V(m/s)")
    velocityEntry=Entry(Point(277.13,70),4)
    velocityEntry.setText(0)
    
    #initialize the height text
    height=Text(Point(374.21,70),"h(m)")
    heightEntry=Entry(Point(443.46,70),4)
    heightEntry.setText(0)
    
    #initialize the ouput reminder
    output=Text(Point(600,70),"Distance(m)")
    # start=Text(Point(69.25,297.5),"start")
    # startBox=Rectangle(Point(41.55,323.75),Point(96.95,271.25))
    # startBox.setFill("Red")
    
    #put theta,velocity,height and their entries on window
    theta.draw(win)
    thetaEntry.draw(win)
    velocity.draw(win)
    velocityEntry.draw(win)
    height.draw(win)
    heightEntry.draw(win)
    #put output reminder on window
    output.draw(win)
    
    # start.draw(win)
    # startBox.draw(win)
    return thetaEntry,velocityEntry,heightEntry

"""initialize the graphic objects when static,
including start button,outline,projectile, and height"""
def static(win):
    #initialize the outline and the start button
    outline=Rectangle(Point(37,770),Point(990,120))
    axis=Line(Point(60,735),Point(980,735))
    axis.setWidth(2)
    outline.draw(win)
    axis.draw(win)
    button=Start(win)
    
    #initialize the projectile and height when static
    #draw the angle of the projectile
    bmb=Projectile(45,0,0)
    bmb.drawP(win)
    bmb.length(win)
    h=HeightPic(0)
    h.drawH(win)
    
    return button,h,bmb

#get text user input from entry    
def entry(thetaEntry,velocityEntry,heightEntry):
    thta=thetaEntry.getText()
    v=velocityEntry.getText()
    h=heightEntry.getText()
    return thta,v,h

# if('__name__'=='__main__'):
main()   
    