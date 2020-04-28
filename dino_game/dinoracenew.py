import pyautogui

import time

class cordinates():
    replay=(960,450)
    dino=(663,464)
    spbreak1=(1000,470)
    spbreak2=(1100,470)

    #740
def restartgame():
    pyautogui.click(cordinates.replay)


restartgame()


    


def speedcal():
    speed=0
    
    tester1=pyautogui.pixel(cordinates.spbreak1[0],cordinates.spbreak1[1])
    tester2=pyautogui.pixel(cordinates.spbreak2[0],cordinates.spbreak2[1])
    distance=100

    if tester2[0]!=247:
        start=time.time()

    if tester1[0]!=247:
        done=time.time()
        jumpstart=time.time()
        elapsed_time=done-start
        if elapsed_time!=0:
            speed=distance/elapsed_time
            print(speed)


  
    tester3=pyautogui.pixel(760,470)
    print(tester3[0])
    
    if tester3[0]!=247:
        
       
        pyautogui.keyDown('space')
        time.sleep(0.05)
        print("jump")
        pyautogui.keyUp('space')


while True:
    
    speedcal()




        
        
        
