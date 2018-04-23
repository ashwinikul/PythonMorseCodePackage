# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 14:24:41 2018

@author: Ashwini
"""

import time
import winsound
import re
morseDict = {'':'','a':'.-','b':'-...','c':'-.-.','d':'-..','e':'.','f':'..-.','g':'--.',
             'h':'....','i':'..','j':'.---','k':'-.-','l':'.-..','m':'--','n':'-.',
             'o':'---','p':'.--.','q':'--.-','r':'.-.','s':'...','t':'-','u':'..-','v':'...-','w':'.--','x':'-..-','y':'-.--','z':'--..',
             '1':'.----','2':'..---','3':'...--','4':'....-','5':'.....','6':'-....','7':'--...','8':'---..','9':'----.','0':'-----',
             '.':'.-.-.-',',':'--..--','?':'..--..','/':'-..-.','@':'.--.-.'}
frequency=2500

def wordToMorseSound(w):
    w= re.sub('[^0-9a-z@,. ]','', w)
    for let in w:
        print(let)
        if let!=' ':
            symbols=morseDict.get(let)
            for sym in symbols:
                #print(sym)
                if sym =='.':
                    winsound.Beep(frequency, 500)
                
                else :
                    winsound.Beep(frequency, 1500)
                #time.wait(1)
                time.sleep(0.5)
        else:
            time.sleep(3.5) 
        time.sleep(1.5)   


def wordToMorseCode(w):
    w= re.sub('[^0-9a-z@,. ]','', w)
    mcode=''
    for let in w:

        if let!=' ':
            symbols=morseDict.get(let)
            mcode=mcode+symbols+'  '
        else:
            mcode=mcode+'   '
    
    mcode= mcode.strip()
        
    return mcode

def morseCodetoLang(w):
    w=re.sub('[^-. ]','', w)
    words = w.split('   ')
    keyValue=''
    
    for w in words:
        lets = w.split('  ')
        
        for l in lets:
            l=l.strip()
            
            keyV= [key for key, value in morseDict.iteritems() if value == l][0]
        
            keyValue=keyValue+keyV
        keyValue=keyValue+' '
     
    return keyValue
            
        

'''



wordspace = 7
letterspace =3
inletterspace =1
dash =3

frequency = 2500  # Set Frequency To 2500 Hertz
duration = 4000  # Set Duration To 1000 ms == 1 second

   

winsound.Beep(frequency, duration)
'''