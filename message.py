binary_string = "01110000 01111001 01110100 01101000 01101111 01101110 00100000 01101001 01110011 00100000 01110111 01101111 01101110 01100100 01100101 01110010 01100110 01110101 01101100"

binary_values = binary_string.split()

# Decode a decimal value to its character
# character = chr(decimal)

# Encode a character to its decimal value
# decimal = ord(character)


# for binary in binary_values:
#     print("Converting:", binary, end=" ... ")

#     # Binary to decimal
#     number = int(binary, base=2)
#     print(number, end=" ... ")

#     # Decimal to character
#     character = chr(number)
#     print(character)



# Decimal numbers in, decoded string out
def decode(encoded):
    characters = []
    for number in encoded:
        char = chr(number)
        characters.append(char)
    message = "".join(characters)
    return message


# Decoded string in, decimal numbers out
def encode(message):
    # Loop over all characters in the message
    # Convert each character
    # Add to the list
    encoded = []
    for char in message:
        number = ord(char)
        encoded.append(number)
    return encoded


message = input("Enter message: ")
numbers = encode(message)

print("Encoded message:", numbers)

decoded_message = decode(numbers)
print("Decoded message:", decoded_message)


class A:
    pass


print(A())