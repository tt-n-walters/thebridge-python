
# for variable in range(49):
#     print("x ", end="")
#     if variable % 7 == 6:
#         print()


# for i in range(7):
#     print("x " * 7)


# for i in range(7):
#     for j in range(7):
#         print("x ", end="")
#     print()




for i in range(7):
    for j in range(7):
        if i == 3 or j == 4:
            print("x ", end="")
        else:
            print("- ", end="")
    print()

print()


for i in range(7):
    for j in range(7):
        print(str(i) + str(j), end=" ")
    print()
