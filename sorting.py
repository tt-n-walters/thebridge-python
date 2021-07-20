import random
import time

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3]


def random_sort(numbers):
    while not numbers == sorted(numbers):
        random.shuffle(numbers)
    return True


def miracle_sort(numbers):
    while not numbers == sorted(numbers):
        time.sleep(1)
    return True


from visualiser import display
# Bubble sort
# Pancake sort
display(numbers)

for j in range(len(numbers)):
    largest = 0
    index = 0
    for i in range(len(numbers) - j):
        n = numbers[i]
        if n >= largest:
            largest = n
            index = i

    input()
    display(numbers, highlight=range(0,index+1))


    selected = numbers[0:index+1]       # Select start to largest
    reversed = selected[::-1]           # Reverse selected
    all = reversed + numbers[index+1:]
    numbers = all[:len(numbers)-j:-1] + numbers[-j:]                # Flip the entire numbers
    
    input()
    display(all, highlight=range(0,index+1))
    input()
    display(all)
    input()
    display(numbers)