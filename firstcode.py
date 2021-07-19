# Fizzbuzz
# Multiple of 3 = Fizz
# Multiple of 5 = Buzz
# 1,2,3,4,5,6,7,8,9...., 100
# 1,2,Fizz,4,5,Fizz,7,8,Fizz
# 1,2,Fizz,4,Buzz,Fizz,7,8,Fizz,Buzz,11,Fizz,13,14,FizzBuzz


# Get all the natural numbers (integers) between 1 and 100
for number in range(1, 101):
    # If the number is a multiple of both 3 and 5, display FizzBuzz
    # If not, check the other two conditions

    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    else:
        # If the number is a multiple of 3, display "Fizz"
        if number % 3 == 0:
            print("Fizz")
        else:
            # If it's multiple of 5, display "Buzz"
            # Otherwise, displat the number itself
            if number % 5 == 0:
                print("Buzz")
            else:
                print(number)
