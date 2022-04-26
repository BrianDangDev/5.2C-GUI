from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

## hardware
led = LED(18)
led2 = LED(23)
led3 = LED(24)


## GUI DEFINITIONS
win = Tk()
win.title("LED Controller")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")

## Event functions
def ledToggle():
    if led.is_lit:
       led.off()
       ledButton["text"] = "Turn Red LED on "
    else:
        led.on()
        ledButton["text"] = "Turn Red LED off"

def led2Toggle():
    if led2.is_lit:
        led2.off()
        led2Button["text"] = "Turn Yellow LED on "
    else:
        led2.on()
        led2Button["text"] = "Turn Yellow LED off"
       
def led3Toggle():
    if led3.is_lit:
        led3.off()
        led3Button["text"] = "Turn Green LED on "
    else:
        led3.on()
        led3Button["text"] = "Turn Green LED off"


def close():
    RPi.GPIO.cleanup()
    win.destroy()
   
## Widget
ledButton = Button(win, text = ' Turn Red LED On', font = myFont, command = ledToggle, bg = 'bisque2', height = 1, width = 24)
ledButton.grid(row=0,column=1)

led2Button = Button(win, text = ' Turn Yellow LED On', font = myFont, command = led2Toggle, bg = 'bisque2', height = 1, width = 24)
led2Button.grid(row=1,column=1)

led3Button = Button(win, text = ' Turn Green LED On', font = myFont, command = led3Toggle, bg = 'bisque2', height = 1, width = 24)
led3Button.grid(row=2,column=1)

exitbutton = Button(win, text = ' Exit', font = myFont, command = close, bg = 'red', height = 1, width = 6)
exitbutton.grid(row=3,column=1)

win.protocol("WM_DELETE_WINDOW", close) #exit cleanly
win.mainloop()