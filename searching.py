
people = ["harry", "ron", "hermione", "fred", "george", "ginny", "dumbledore", "voldemort"]
people.sort()
print("Sorted:", people)

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
    left = 0
    right = len(data) - 1
    while left < right:
        midpoint = left + (right - left) // 2
        name = data[midpoint]

        if name == target:
            print("Found", target, "at", midpoint)
            return midpoint
        elif name < target:
            left = midpoint + 1
        elif name > target:
            right = midpoint - 1



linear_search(people, "ron")
binary_search(people, "percy")