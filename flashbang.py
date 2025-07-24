#flashbang v0.001

#-----------------------------------#
#  - twitch chat donation/ point redeem triggers call to execute this file
#  - program plays sound in background
#  - program sends command to windows create handle
#  - program decreases alpha val and destroys window after set iterations
#-----------------------------------#

import time
from pygame import mixer
from tkinter import *
from win32 import win32api
import pywintypes, win32con
from PIL import Image, ImageTk

def main():
    mixer.init()
    mixer.music.load('chucklenut.mp3')
    mixer.music.play()

    time.sleep(1)

    bang()

    # Optional wait period after getting flashbanged
    #cooldown()



def bang(): 
    # Create Tk object
    root = Tk() 
    
    # Create flashbang window
    root.attributes('-alpha',0.95) #         <-- edit this to change opacity
    root.wm_attributes('-fullscreen',True) 
    root.wm_attributes("-topmost", True)
    root.wm_attributes("-disabled", True)
    root.lift()

    img = Image.open("brick.jpg")
    img = ImageTk.PhotoImage(img)
    img_label = Label(root, image=img)
    img_label.pack()

    timeAfter = 300
    alphaVal = 0.9
    i = 0
    
    # I really wanted this to work but its like mixing oop with procedural and only updates a single time at the end.
    # for i in range(10):
    #     print(alphaVal)
    #     #looking at variable after the fact after calculations have already happened
    #     root.after(timeAfter, lambda: root.attributes("-alpha", (alphaVal)))
    #     time.sleep(1)
    #     timeAfter += 300
    #     alphaVal -= 0.05
    

    # Nothing like manually setting window opacity :|
    root.after(300, lambda: root.attributes("-alpha", 0.9))
    root.after(600, lambda: root.attributes("-alpha", 0.85))
    root.after(900, lambda: root.attributes("-alpha", 0.8))
    root.after(1200, lambda: root.attributes("-alpha", 0.75))
    root.after(1500, lambda: root.attributes("-alpha", 0.7))
    root.after(1800, lambda: root.attributes("-alpha", 0.65))
    root.after(2100, lambda: root.attributes("-alpha", 0.6))
    root.after(2400, lambda: root.attributes("-alpha", 0.55))
    root.after(2700, lambda: root.attributes("-alpha", 0.5))
    
    
    root.after(3000, lambda: root.destroy())

    # Convert tkinter window into Handle object
    hWindow = pywintypes.HANDLE(int(root.frame(), 16))

    # Set new properties for window
    exStyle = win32con.WS_EX_COMPOSITED | win32con.WS_EX_LAYERED | win32con.WS_EX_TOPMOST | win32con.WS_EX_TRANSPARENT
    win32api.SetWindowLong(hWindow, win32con.GWL_EXSTYLE, exStyle)

    # Execute mainloop
    root.mainloop()


def cooldown():
    for x in range(300):
        time.sleep(1)
        print(300 - x)

    


if __name__ == '__main__':
    main()