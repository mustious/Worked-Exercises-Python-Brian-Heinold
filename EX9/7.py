import sys

text = input("Enter the text: ")
letter = input("Enter the letter: ")

i = 0
while i < len(text):
    if letter == text[i]:
        break
        print("The index of '{}' in the text is {}".format(letter, i))
        sys.exit()
    i += 1

print("The string does not contain {}".format(letter))

