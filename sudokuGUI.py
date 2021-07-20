import tkinter as tk


def tile_clicked(event):
    label = event.widget
    label["background"] = "yellow"
    
    name = str(label)
    if name == ".!label":
        number = 0
    else:
        number = int(name.strip(".!label")) - 1
    row = number // 9
    column = number % 9

    def keypressed(event):
        if event.char.isdigit():
            number_typed = event.char
            label["text"] = number_typed
        window.unbind("<Key>")
        label["background"] = "white"

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