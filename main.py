import pyautogui as pt
from time import sleep
import pyperclip
import random

sleep(3)

pos1 = pt.locateOnScreen("emoji_attachment.png",confidence=0.6)
x = pos1[0]
y = pos1[1]

def rec_msg():
    global x,y

    pos = pt.locateOnScreen("emoji_attachment.png",confidence=0.6)
    x = pos1[0]
    y = pos1[1]
    pt.moveTo(x,y,duration=0.05)
    pt.moveTo(x + 70,y-40, duration = .5)
    pt.tripleClick()
    pt.rightClick()
    pt.moveRel(12,15)
    pt.click()
    whts_msg =pyperclip.paste()
    print("Message recieved:"+whts_msg)
    pt.click()
    return whts_msg

def response(msg):
    global x,y

    pos = pt.locateOnScreen("emoji_attachment.png",confidence=0.6)
    x = pos1[0]
    y = pos1[1]
    pt.moveTo(x+200,y+20,duration=.5)
    pt.click()
    pt.typewrite(msg,interval = 0.1)
    pt.typewrite("\n",interval=.01)

def msg_reply(msg):
    randno = random.randrange(3)
    if "?"in str(msg).lower():
        return "I don't know"
    else:
        if randno==0:
            return "I'll chat later"
        elif randno==1:
            return "Ok"
        else:
            return "Busy right now..."

def check_msgs():
    pt.moveTo(x+50,y-35,duration=.5)
    while True:
        try:
            pos = pt.locateOnScreen("notification.png",confidence=.7)
            if pos is not None:
                pt.moveTo(pos[0]-100,pos[1])
                pt.click()
                sleep(.5)

        except(Exception):
            print("No new messages located")

        if pt.pixelMatchesColor(int(x+50),int(y-35),(255,255,255),tolerance=10):
            print("is white")
            processed_message =  msg_reply(rec_msg())
            response(processed_message)
        else:
            print("no new messages")
        sleep(5)

check_msgs()
