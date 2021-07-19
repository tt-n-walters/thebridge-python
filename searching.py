
people = ["harry", "ron", "hermione", "fred", "george", "ginny", "dumbledore", "voldemort"]
people.sort()

# Where (index) of george
# position = people.index("george")
# print("Found george at", position)


# Linear search algorithm
def linear_search(data, target):
    for i in range(len(data)):
        name = data[i]
        if name == target:
            print("Found", target, "at", i)
            return i


# Binary search
def binary_search(data, target):
    counter = 0
    left = 0
    right = len(data) - 1
    while left < right:
        counter = counter + 1
        midpoint = left + (right - left) // 2
        name = data[midpoint]

        if name == target:
            print("Found", target, "at", midpoint)
            print("Counter:", counter)
            return midpoint
        elif name < target:
            left = midpoint + 1
        elif name > target:
            right = midpoint - 1



file = open("names_ages.csv", "r")
contents = file.read()
lines = contents.splitlines()
lines.sort()
file.close()

names = []
ages = []
for line in lines:
    line = line.split(",")
    name = line[0]
    age = int(line[1])
    names.append(name)
    ages.append(age)

target = "Fiamma Enero"

print("Searching...")
index = linear_search(names, target)
age = ages[index]
print(target, "is", age, "years old.")

index = binary_search(names, target)
age = ages[index]
print(target, "is", age, "years old.")
