#flashbang v0.001

#-----------------------------------#
#  - twitch chat donation/ point redeem triggers call to execute this file
#  - program plays sound in background
#  - program sends command to windows create handle
#  - program decreases opacity of window and destroys it after set iterations
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

    bang(iters=15, starting_opacity=100, ending_opacity=0)

    # Optional wait period after getting flashbanged
    # cooldown()



def bang(iters, starting_opacity, ending_opacity): 
    # Create Tk object
    root = Tk() 
    
    # Create flashbang window
    root.attributes('-alpha', 1.00) #         
    root.wm_attributes('-fullscreen',True) 
    root.wm_attributes("-topmost", True)
    root.wm_attributes("-disabled", True)
    root.lift()

    # OPTIONAL: Comment this out for just a blank white screen.
    img = Image.open("brick.jpg")
    img = ImageTk.PhotoImage(img)
    img_label = Label(root, image=img)
    img_label.pack()

    time_after = 300
    increment = (starting_opacity - ending_opacity) / iters
    
    # We can get around python not passing vars by value by waiting manualy a couple ms in between each root.after() call
    for i in range(iters):
        
        # Divide opacity by 100 to get percent val between (0,1)
        root.after(time_after, lambda: root.attributes("-alpha", ((starting_opacity - (i * increment)) / 100)))
        time.sleep(0.2)
        root.update()
        time_after += 200
    
    
    root.after(time_after, lambda: root.destroy())

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