import random
import string

lower_ascii = string.ascii_lowercase
upper_ascii = string.ascii_uppercase
numbers = string.digits
punc = string.punctuation

all_chars = list(lower_ascii + upper_ascii + numbers + punc)
selected_char = []

while len(selected_char) < 8:
    char_random = random.choice(all_chars)
    if char_random not in selected_char:
        selected_char.append(char_random)

selected_char = selected_char * 2
random.shuffle(selected_char)

for i in range(0, 4):
    print(" ".join(selected_char[i*4:i*4 +4]))