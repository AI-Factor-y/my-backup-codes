import pyautogui
import speech_recognition as sr
import os
from time import gmtime
import time

def recognition(time=2):
    
   
 
    r=sr.Recognizer() 
    with sr.Microphone() as source:
        
        print('say something ')
        audio=r.listen(source,timeout=time)
    
    try:
        text=r.recognize_google(audio)
        print(text)
    except Exception as e:
         print(e)

    return text

def speaker(  speak_word  ,  test_word  ,  rec_text  ,  action=' '  ):      #creates file and outputs for voice
    if rec_text==test_word:
        word="at you service"
        f=open("C:\\Users\\USER\\Desktop\\filet.vbs","w+")
        f.write('set sapi=createobject("sapi.spvoice")\n')
        f.write('sapi.speak "')
        f.write(speak_word)
        f.write('"')


        f.close()#time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
        
        os.startfile("C:\\Users\\USER\\Desktop\\filet.vbs")

        if action!=' ':
            
            os.startfile(action)

while True:

   
    daytime=time.strftime("%a, %d %b ", gmtime())
    rec=recognition()
    speaker("opening firefox sir","Jarvis open Firefox",rec,"C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe")
    speaker("at your service sir,","Jarvis",rec)
    speaker(daytime,"jarvis what's today's date",rec)
    if rec=="Jarvis let's return":
        speaker("returning to home","Jarvis let's return",rec)
        pyautogui.click(1918,1050)

    
        
    time.sleep(3)
    
    
