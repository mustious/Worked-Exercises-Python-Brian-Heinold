import random

text = input("Enter a text: ")

len_text = len(text)
text_list = list(text)

random.shuffle(text_list)
shuffled_text = "".join(text_list)
print(shuffled_text)