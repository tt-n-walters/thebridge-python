from math import floor
import time


def display_puzzle(puzzle):
    output = "\u001b[J\u001b[H"
    for j in range(len(puzzle)):
        row = puzzle[j]
        if j % 3 == 0:
            output += " +-------+-------+-------+\n"
        for i in range(len(row)):
            number = row[i]
            if i % 3 == 0:
                output += " |"
            output += " "
            if number > 0:
                output += str(number)
            else:
                output += " "
        output += " |\n"
    output += " +-------+-------+-------+"
    print(output)


positions_checked = 0


def check_position(puzzle_data, row, column, n):
    global positions_checked
    positions_checked += 1
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



file = open("puzzles.txt", "r")
file_contents = file.read()
file.close()

# Process the file contents
# Split up into the 50 puzzles
puzzles = file_contents.splitlines()

# Take just the first puzzle, for now.
puzzle = puzzles[30]

# Loop through all 81 digits of a puzzle
puzzle_data = []
for i in range(len(puzzle)):
    # Every 9 numbers, add a new row
    if i % 9 == 0:
        puzzle_data.append([])
    number = int(puzzle[i])
    puzzle_data[-1].append(number)


mistake_counter = 0


def solve_sudoku(puzzle_data):
    global mistake_counter
    # Recursive, hueristic-based, backtracking, algorithm
    # Try to solve the puzzle
    # Step 1 Find an empty spot
    display_puzzle(puzzle_data)
    time.sleep(0.01)
    for row in range(9):
        for column in range(9):
            number = puzzle_data[row][column]
            # print("Looking at:", number)
            if number == 0:
                # print("Found a zero.")

                # Step 2 Check numbers 1-9, see if they fit in the empty spot
                for n in range(1, 10):
                    # print("\nChecking", n)
                    
                    # Step 3 Guess a number
                    if check_position(puzzle_data, row, column, n):
                        
                        # Step 4 Move on, and try the next empty spot
                        puzzle_data[row][column] = n
                        solve_sudoku(puzzle_data)
                    
                # Step 5 Undo an incorrect guess
                puzzle_data[row][column] = 0
                mistake_counter = mistake_counter + 1
                return
    
    # After solving, stop
    display_puzzle(puzzle_data)
    print("Mistakes:", mistake_counter)
    print("Positions checked:", positions_checked)
    exit()


puzzle_data[0][0] = 0
puzzle_data[0][3] = 0
puzzle_data[0][4] = 0
puzzle_data[1][0] = 0
puzzle_data[1][1] = 0
puzzle_data[3][5] = 0
puzzle_data[6][0] = 0
puzzle_data[6][5] = 0
puzzle_data[6][6] = 0
puzzle_data[7][1] = 0
puzzle_data[4][5] = 0
puzzle_data[4][7] = 0
puzzle_data[4][6] = 0

display_puzzle(puzzle_data)
solve_sudoku(puzzle_data)
