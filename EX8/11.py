import random

text = input("Enter your text: ")
text_list = list(text)
anagram = ""

i = 0
while len(text_list) > 0:
    a_choice = random.choice(text_list)
    anagram += a_choice
    text_list.remove(a_choice)
    i += 1
print(anagram)