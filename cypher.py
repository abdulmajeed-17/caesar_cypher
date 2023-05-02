import sys
converted_data = ""
position = -1
# function that changes each character by shifting it based on a certain number passed in as input
def encoder(letter):
    if ord(letter) + int(sys.argv[1]) > 90 and int(sys.argv[1]) > 26:
        return chr(ord(letter) + int(sys.argv[1]) - (26 * (int(sys.argv[1])//26))).upper()
    elif ord(letter) + int(sys.argv[1]) > 90 and int(sys.argv[1]) < 26:
        return chr(ord(letter) + int(sys.argv[1]) - 26).upper()
    else:
        return chr(ord(letter) + int(sys.argv[1])).upper()
# obtains the raw message from the terminal
for line in sys.stdin:
    raw = line
    break
# filters the message by making it upper case and removing any non-alphabetic character
for character in raw:
    if character.isalpha(): 
        converted_data += character.upper()
# displays the data in the form of blocked matrix, which consists of 10 five-character words per line
for letter in converted_data:
    position += 1
    encode = encoder(letter)
    if position == 50:
        print()
        position = 0
        print(encode, end="")
    elif position % 5 == 0 and position != 0:
        print(" ", end="")
        print(encode, end="")
    else: print(encode, end="")