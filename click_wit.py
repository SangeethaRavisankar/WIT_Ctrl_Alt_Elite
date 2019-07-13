# UNSW - WIT HACKATHON
# PROJECT NAME: CLICK! 
# AUTHORS : ELAKKIYA, JAGADISH, SANGEETHA
# 

from bs4 import BeautifulSoup
from gtts import gTTS 
from copy import deepcopy
from random import randint

import wikipedia
import requests
import webbrowser
import time
import os 

def recordChoiceAudio(summText):
    myobj = gTTS(text=summText, lang=language, slow=False) 
    myobj.save("cwit.mp3") 
    os.system("mpg321 cwit.mp3")
    webbrowser.open(r"C:\Users\SriVigneshwarRavi\cwit.mp3")

def recordAudio(summText):
    myobj = gTTS(text=summText, lang=language, slow=False) 
    myobj.save("wit.mp3") 
    os.system("mpg321 wit.mp3")
    webbrowser.open(r"C:\Users\SriVigneshwarRavi\wit.mp3")
    
# Language in which you want to convert 
language = 'en'
choice=-1
choice1=-1

while(choice!=0):
    searchKey = input("What do you wanna search? \n")

    response = requests.get(wikipedia.page(searchKey).url)
    soup = BeautifulSoup(response.content, "html.parser")

    titleList = [item.get_text() for item in soup.select("h2 .mw-headline")]
    print(titleList)

    recordChoiceAudio("Say 1 to listen to the summary or 2 to listen the titles")
    time.sleep(1)
    titleList1=deepcopy(titleList)
    cont = wikipedia.page(searchKey).content

    #choice = randint(1,2)
    choice = 2
    if choice == 1:
        summText = wikipedia.summary(searchKey)
        recordAudio(summText)

    if choice == 2:
        
        time.sleep(3)
        for i in range(len(titleList)):
            titleList1[i]=str(i+1)+" for " +titleList[i] + " "
        str1 = ' '.join(titleList1)
        recordAudio(str1)
        time.sleep(5)
        choice1 = randint(1,len(titleList))
        
        while(choice1!=0):
            recordAudio("Pick a number for related content or say 0 to continue with different search")
            time.sleep(2)
            print(choice1)
            print(titleList[choice1-1])
            conth = cont.find(titleList[choice1-1])
            contt = cont.find("\n==",conth)
            head = cont[conth:contt]
            print(choice,head)
            head = head.replace("=","")
            try:
                recordAudio(head)
                choice1=0
            except:
                recordAudio("No content to display")
                choice1 = randint(1,len(titleList))
                #time.sleep(2)
                continue