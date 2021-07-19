minimum = 1
maximum = 100000

while True:
    guess = minimum + (maximum - minimum) // 2
    print("Guess:", guess)

    feedback = input("Feedback: ")
    if feedback == "correct":
        print("Python is the best.")
        break
    elif feedback == "too low":
        minimum = guess + 1
    elif feedback == "too high":
        maximum = guess - 1
