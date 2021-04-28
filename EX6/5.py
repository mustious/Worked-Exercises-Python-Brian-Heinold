text = input("enter your text: ")
text = list(text)
text[1] = "*"
new_string = "".join(text) + "!!!"
print(new_string)