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

# Functions to convert input text to audio
def recordChoiceAudio(summText):
    audFile = gTTS(text=summText, lang=language, slow=False) 
    audFile.save("cwit.mp3") 
    os.system("mpg321 cwit.mp3")
    webbrowser.open(r"C:\Users\SriVigneshwarRavi\cwit.mp3")
    time.sleep(2)

def recordAudio(summText):
    audFile = gTTS(text=summText, lang=language, slow=False) 
    audFile.save("wit.mp3") 
    os.system("mpg321 wit.mp3")
    webbrowser.open(r"C:\Users\SriVigneshwarRavi\wit.mp3")
    time.sleep(2)
    
# Language in which we want to convert 
language = 'en' # en - English, fr - French

#Initializations
choice=-1
choice1=-1
search=[]

# Until the user wants to quit
intro = "What do you wanna search?"
while(choice!=0):
    
    recordChoiceAudio(intro)
    searchK = input(intro)
    
    # Try to get relevant searchs limited to 2
    search = wikipedia.search(searchK,results=2)
    print(search)
    
    try:
        response = requests.get(wikipedia.page(search[0]).url)
        searchKey = search[0]
    except:
        response = requests.get(wikipedia.page(search[1]).url)
        searchKey = search[1]
    
    recordChoiceAudio("Say 1 to listen to the summary or 2 to listen the titles")
    soup = BeautifulSoup(response.content, "html.parser")
    titleList = [item.get_text() for item in soup.select("h2 .mw-headline")]
    time.sleep(1)
    titleList1=deepcopy(titleList[:-4])
    print(titleList1)
    cont = wikipedia.page(searchKey).content

    #choice = randint(1,2)
    choice = 2
    
    
    if choice == 1:
        summText = wikipedia.summary(searchKey)
        recordAudio(summText)

    if choice == 2:
        #time.sleep(3)
        for i in range(len(titleList)-4):
            titleList1[i]=str(i+1)+" for " +titleList[i] + " "
        str1 = ' '.join(titleList1)
        recordAudio(str1)
        time.sleep(10)
        choice1 = randint(1,len(titleList)-4)
        
        while(choice1!=0):
            recordAudio("Pick a number for related content or say 0 to continue with different search")
            time.sleep(2)
            print(choice1)
            print(titleList[choice1-1])
            conth = cont.find(titleList[choice1-1])
            contt = cont.find("\n==",conth)
            head = cont[conth:contt]
            print(head)
            head = head.replace("=","")
            if len(head.split()) > 10:
                recordAudio(head)
                time.sleep(100)
                choice1=0
            else:
                recordAudio("No content to display")
                choice1 = randint(1,len(titleList)-4)
                #time.sleep(2)
                continue