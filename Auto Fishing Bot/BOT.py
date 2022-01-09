from keys import PressKey, ReleaseKey, numpad4, numpad5, numpad6, numpad7, numpad8, numpad9, W, A, S, D
import pyautogui as pag
import keyboard
import time
import random
import win32api
import win32con
from pyautogui import*

#redefinings


#variables

x = 1300
y = 10
height = 30
length = 150
c = 0.98

sleep = 0.2

while 1:
    a = random.random()
    b = random.randint(3,5)
    
    

    if pag.locateOnScreen('a.PNG',confidence = c, region=(x,y,length,height)) != None:
        print("A")
        print(round(a,2))
        print(b)

        PressKey(A)
        time.sleep((b/10) + (a/10))
        ReleaseKey(A)

        time.sleep (b)

        # pag.keyDown("num4")
        # pag.keyUp("num4")
    else:
        # print ("CAN'T SEE NUM 4")
        time.sleep(sleep)


    if pag.locateOnScreen('s.png',confidence = c, region=(x,y,length,height)) != None:
        print("S")
        print(round(a,2))
        print(b)

        PressKey(S)
        time.sleep((b/10) + (a/10))
        ReleaseKey(S)

        time.sleep (b)
        
        # pag.keyDown("num5")
        # pag.keyUp("num5")
    else:
        # print ("CAN'T SEE NUM 5")
        time.sleep(sleep)


    if pag.locateOnScreen('d.png',confidence = c, region=(x,y,length,height)) != None:
        print("D")
        print(round(a,2))
        print(b)

        PressKey(D)
        time.sleep((b/10) + (a/10))
        ReleaseKey(D)

        time.sleep (b)

        # pag.keyDown("num6")
        # pag.keyUp("num6")
    else:
        # print ("CAN'T SEE NUM 6")
        time.sleep(sleep)


    if pag.locateOnScreen('w.png',confidence = c, region=(x,y,length,height)) != None:
        print("W")
        print(round(a,2))
        print(b)

        PressKey(W)
        time.sleep((b/10) + (a/10))
        ReleaseKey(W)

        time.sleep (b)

        # pag.keyDown("num7")
        # pag.keyUp("num7")
    else:
        # print ("CAN'T SEE NUM 7")
        time.sleep(sleep)


    # if pag.locateOnScreen('num8.png',confidence = c, region=(x,y,length,height)) != None:
    #     print("NUM8")
    #     print(round(a,2))

    #     PressKey(numpad4)
    #     time.sleep(a+a)
    #     ReleaseKey(numpad4)

    #     # pag.keyDown("num8")
    #     # pag.keyUp("num8")
    # else:
    #     # print ("CAN'T SEE NUM 8")
    #     time.sleep(sleep)


    # if pag.locateOnScreen('num9.png',confidence = c, region=(x,y,length,height)) != None:
    #     print("NUM9")
    #     print(round(a,2))

    #     PressKey(numpad4)
    #     time.sleep(a+a)
    #     ReleaseKey(numpad4)

    #     # pag.keyDown("num9")
    #     # pag.keyUp("num9")
    # else:
    #     # print ("CAN'T SEE NUM 9")
    #     time.sleep(sleep)
   
