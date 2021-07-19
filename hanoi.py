
# Tail-end optimised, recursive, iterating, algorithm



def move(origin, destination):
    print("[", origin, ",", destination, "],")
    # file.write("[{},{}],".format(origin, destination))



def move_lots(n_disks, origin, destination, other):
    if n_disks == 0:   # If there are zero disks to move
        return         # do nothing.

    move_lots(n_disks - 1, origin, other, destination)
    move(origin, destination)
    move_lots(n_disks - 1, other, destination, origin)


move_lots(3, 0, 2, 1)
