text = input("Enter your word: ")

a_index = text.index("a")
print(text[:a_index+1])
print(text[a_index+1:])
