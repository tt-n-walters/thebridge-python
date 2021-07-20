import tkinter
import random


# Create window
window = tkinter.Tk()


def roll_die():
    print("Rolling die...")
    number = random.randint(1, 6)
    label["text"] = number
    # roll_die.counter = roll_die.counter + 1
    # if roll_die.counter < 30:
    #     window.after(50, roll_die)

    if roll_die.is_rolling == True:
        window.after(50, roll_die)


def start_dice_roll():
    print("Starting to roll the die...")
    # roll_die.counter = 0

    roll_die.is_rolling = True
    roll_die()
    window.after(3000, stop_rolling)


def stop_rolling():
    roll_die.is_rolling = False

# Create the widget
label = tkinter.Label()
button = tkinter.Button(text="Roll die")

# Customisation
window["background"] = "white"
label["font"] = ("Charlemagne Std", 60)
label["width"] = 1
label["background"] = "white"
label["foreground"] = "navy"
button["font"] = ("Candara", 14)
button["background"] = "white"
button["command"] = start_dice_roll

# Add the widget to screen
label.pack(padx=60, pady=30)
button.pack(pady=10, )

tkinter.mainloop()


