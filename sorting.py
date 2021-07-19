import random
import time

numbers = [3, 1, 4, 1, 5, 9, 2]


def random_sort(numbers):
    while not numbers == sorted(numbers):
        random.shuffle(numbers)
    return True


def miracle_sort(numbers):
    while not numbers == sorted(numbers):
        time.sleep(1)
    return True


print(numbers)
miracle_sort(numbers)
print(numbers)

