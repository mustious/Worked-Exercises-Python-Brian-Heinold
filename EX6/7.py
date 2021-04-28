text = input("Enter your text: ")

text_reverse = text[-1::-1]

if text == text_reverse:
    print("This is a palindrome")
else:
    print("Not a palidrome")