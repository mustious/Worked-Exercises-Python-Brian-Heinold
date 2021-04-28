import string
all_alpha = string.ascii_lowercase

for i in range(26):
    text = all_alpha[i:] + all_alpha[:i]
    print(text)