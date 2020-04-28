import pyautogui
import speech_recognition as sr
import os
from time import gmtime
import time

def recognition(time=3):
    
   
 
    r=sr.Recognizer() 
    with sr.Microphone() as source:
       
        print('say something ')
        audio=r.listen(source)
    IBM_USERNAME="abhinavhariharan2001@gmail.com"
    IBM_PASSWORD="Shyja2001"
    
    try:
        text=r.recognize_ibm(audio,"https://gateway-lon.watsonplatform.net/speech-to-text/api","NX-2ipFvJLq_qXRIqIrLmWt4B1p4250x6MikTlxmMBX_")
        print(text)
    except sr.UnknownValueError:
        print("could not get what you said")
    except sr.RequestError as e:
        print("couldnt get : {0}".format(e))

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
    
    
