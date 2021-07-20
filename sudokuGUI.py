import tkinter as tk


def tile_clicked(event):
    # Get the widget that was clicked on, highlight it
    label = event.widget
    label["background"] = "yellow"

    # Work out the tile's position, based on the number in the name
    name = str(label)
    if name == ".!label":
        number = 0
    else:
        number = int(name.strip(".!label")) - 1
    row = number // 9
    column = number % 9

    # Keypress event to allow entering a number into the grid
    def keypressed(event):
        label["background"] = "white"
        if event.char.isdigit() and not event.char == "0":
            number_typed = event.char
            label["text"] = number_typed
        window.unbind("<Key>")

    window.bind("<Key>", keypressed)



window = tk.Tk()

for i in range(9):
    for j in range(9):
        label = tk.Label()
        # label["text"] = str(i) + str(j)
        label["width"] = 2
        label["font"] = ("Consolas", 14)
        label["relief"] = tk.RIDGE
        label["background"] = "white"
        label.bind("<Button-1>" , tile_clicked)
        

        label.grid(column=j, row=i, ipadx=5, ipady=5)

window.mainloop()