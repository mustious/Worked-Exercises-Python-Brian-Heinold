import string
import random

text = input("Please enter a message to be encrypted: ")
text = text.lower()
print(text)
random_numbers = []

# encrpting text

encrypted_text = ""

for char in text:
    if char in string.ascii_lowercase:
        a_random_number = random.randint(1, 26)
        random_numbers.append(a_random_number)
        char_index = string.ascii_lowercase.index(char)
        new_char_index = (char_index + a_random_number) % 26
        encrypted_text += string.ascii_lowercase[new_char_index]
    else:
        encrypted_text += char

print("Generated random numbers: {}".format(random_numbers))
print("Encrypted text: {}".format(encrypted_text))

# decrypting text
i = 0
decrypted_text = ""

for char in encrypted_text:
    if char in string.ascii_lowercase:
        a_random_number = random_numbers[i]
        i += 1
        char_index = string.ascii_lowercase.index(char)
        new_char_index = (char_index - a_random_number) % 26
        decrypted_text += string.ascii_lowercase[new_char_index]
    else:
        decrypted_text += char

print("Decrypted text: {}".format(decrypted_text))