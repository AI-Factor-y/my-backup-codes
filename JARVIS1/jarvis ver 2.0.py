from __future__ import print_function
import pyautogui
import speech_recognition as sr
import os
from time import gmtime
import time
import random

from flask import Flask ,render_template ,request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

english_bot=ChatBot("Chatterbot",storage_adapter="chatterbot.storage.SQLStorageAdapter")

trainer= ChatterBotCorpusTrainer(english_bot)

trainer.train("C:\\Users\\USER\\AppData\\Local\\Programs\\Python\\Python37-32\\Lib\\site-packages\\chatterbot_corpus\\data\\english")


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

def speaker(  speak_word  ,  test_word   ,  action=' '  ):      #creates file and outputs for voice
    print(test_word)
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

def typer( speak_word  ,  test_word   ,  typer  ):
    
    print(test_word)
    word="at you service"
    f=open("C:\\Users\\USER\\Desktop\\typerfil.vbs","w+")
    f.write('set sapi=createobject("sapi.spvoice")\n')
    f.write('set wshshell=wscript.createobject("wscript.shell")\n')
    f.write('wshshell.sendkeys "')
    f.write('{ENTER}')
    f.write('"\n')
    f.write('wshshell.sendkeys "')
    f.write(typer)
    f.write('"\n')
    f.write('sapi.speak "')
    f.write(speak_word)
    f.write('"')


    f.close()#time.strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
    os.startfile("C:\\Users\\USER\\Desktop\\typerfil.vbs")

    




daytime=time.strftime("%a, %d %b ", gmtime())
#rec=recognition()
print("listening :: >")
time.sleep(3.6)

speaker("yes sir","Jarvis")
print("listening :: >")
time.sleep(8.5)

speaker("well sir,.we have python, java , c and prolog languages on the system.","jarvis create a new project")

print("listening :: >")
time.sleep(10.0)

speaker("entering python mode sir, a new file will be created","jarvis use python","C:\\WINDOWS\\system32\\notepad.exe")
print("listening :: >")
time.sleep(8.0)
speaker("visual library, open cv found sir, ","jarvis import visual library")
typer("imported successfully"," ","import cv2")
print("listening :: >")
time.sleep(10.6)
typer("importing num py","import numpy","import numpy")
print("listening :: >")
time.sleep(8.0)

speaker("keras module not found sir, should we consider  installing it via pip","import keras","C:\\Users\\USER\\AppData\\Local\\Programs\\Python\\Python37-32\\Scripts\\installer.bat")
typer("","","cd scripts")
time.sleep(0.5)
typer("","","{ENTER}")
print("listening :: >")
time.sleep(9)


typer("","","pip install keras")
time.sleep(6)
typer("ok sir ","yes","{ENTER}")




    
time.sleep(3)


