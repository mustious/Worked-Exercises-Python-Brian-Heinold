text = input("Enter text here: ")

text_list = text.strip().split()

print("The third word is {}".format(text_list[2]))

third_words = [text_list[num] for num in range(3, len(text_list)+1, 3)]
print(third_words)