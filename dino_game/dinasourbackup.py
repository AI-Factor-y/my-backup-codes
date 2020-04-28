import pyautogui
import time
from PIL import ImageGrab,ImageOps

from numpy import *


class cordinates():
    replay=(960,450)
    dino=(663,464)
    tree1=(708+26,458)
    tree2=(741+26,498)
    spbreak1=(1000,470)
    spbreak2=(1100,470)

def restartgame():
    pyautogui.click(cordinates.replay)


restartgame()

def space():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    print("jump")
    pyautogui.keyUp('space')
    

restartgame()    
 
#space()

def imagegrab(speed):
   


    box=(cordinates.tree1[0]+speed,cordinates.tree1[1],cordinates.tree2[0]+speed,cordinates.tree2[1])
    image=ImageGrab.grab(box)

    grayImage=ImageOps.grayscale(image)

    a=array(grayImage.getcolors())

    print(a.sum())
    return a.sum()

i=0
rate=6
while True:
    i+=0.4
            
    if (imagegrab(i)!=1567):
        space()

    if pyautogui.locateOnScreen("restart.png",region=(920,430,1000,490)):
        print("generation terminated")

        break

    

    
        
    
    
    

    

