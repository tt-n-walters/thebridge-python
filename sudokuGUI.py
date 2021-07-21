import tkinter as tk
from math import floor


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
            start_solve.puzzle_data[row][column] = int(event.char)
        window.unbind("<Key>")

    window.bind("<Key>", keypressed)

### sudoku code

def check_position(puzzle_data, row, column, n):
    # Check the row
    # print("Checking row.")
    for i in range(9):
        number_in_puzzle = puzzle_data[row][i]
        if n == number_in_puzzle:
            # print("Already in row. Invalid number.")
            return False

    # Check the column
    # print("Checking column.")
    for i in range(9):
        number_in_puzzle = puzzle_data[i][column]
        if n == number_in_puzzle:
            # print("Already in column. Invalid number.")
            return False

    # Check the block
    # print("Checking block.")
    block_x = floor(row / 3) * 3
    block_y = floor(column / 3) * 3
    # Start at the calculated coordinates, get the next 3 numbers
    for i in range(block_x, block_x + 3):
        for j in range(block_y, block_y + 3):
            number_in_puzzle = puzzle_data[i][j]
            if n == number_in_puzzle:
                # print("Already in block. Invalid number.")
                return False

    return True


def solve_sudoku(puzzle_data):
    if any([0 in row for row in puzzle_data]):
        for row in range(9):
            for column in range(9):
                number = puzzle_data[row][column]
                if number == 0:
                    for n in range(1, 10):
                        if check_position(puzzle_data, row, column, n):
                            puzzle_data[row][column] = n
                            puzzle_data = solve_sudoku(puzzle_data)
                        
                    puzzle_data[row][column] = 0
                    return puzzle_data
        
    start_solve.puzzle_data = puzzle_data


def start_solve():
    solve_sudoku(start_solve.puzzle_data)


start_solve.puzzle_data = []
for i in range(9):
    row = [0] * 9
    start_solve.puzzle_data.append(row)


###


### tkinter code

window = tk.Tk()

# Grid to save the 9x9 of labels
grid = []
for i in range(9):
    grid.append([])                # Create the row
    
    for j in range(9):
        label = tk.Label()
        label["width"] = 2
        label["font"] = ("Consolas", 14)
        label["relief"] = tk.RIDGE
        label["background"] = "white"
        
        label.bind("<Button-1>" , tile_clicked)
        label.grid(column=j, row=i, ipadx=5, ipady=5)

        grid[i].append(label)

# Read file and add numbers to puzzle and labels
file = open("puzzles.txt")
puzzle_strings = file.read().splitlines()
file.close()
puzzle = puzzle_strings[0]
for row in range(9):
    for column in range(9):
        index = row * 9 + column
        number = int(puzzle[index])
        start_solve.puzzle_data[row][column] = number


def display_puzzle(puzzle_data):
    for row in range(9):
        for column in range(9):
            number = puzzle_data[row][column]
            if number > 0:
                label = grid[row][column]
                label["text"] = number

def display_button():
    display_puzzle(start_solve.puzzle_data)


button = tk.Button(text="Solve")
button["command"] = start_solve
button.grid(column=9, row=0)

display = tk.Button(text="Display")
display["command"] = display_button
display.grid(column=9, row=1)


window.mainloop()

###