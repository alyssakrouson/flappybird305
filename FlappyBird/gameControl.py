                  gameControl.py                     Modified
import keyboard

x = 0
y = 0
def SpaceBarInput(event):
    global x
    global y

    x += 5
    y += 2
    print(f"X-axis: {x}")

keyboard.on_press_key("space", on_spacebar_press) 
#keep the program 
#running until input is control c
while True:
    pass





