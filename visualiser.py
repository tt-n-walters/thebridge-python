
def display(values, highlight=None):
    output = "\033[0;0H\033[J"
    char = "▅"
    width = max(values)
    for i, n in enumerate(values):
        output += f"{n:>2} "
        for j in range(width):
            if j > n:
                output += " "
            elif highlight and i in highlight:
                output += f"\033[93m{char}\033[0m"
            else:
                output += char
        output += "\n"
    print(output)
