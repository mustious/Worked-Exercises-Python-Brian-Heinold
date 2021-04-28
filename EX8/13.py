text = input("Enter your list of strings seperated by spaces: ")
text_list = text.strip().split()

print([a_string[1:] for a_string in text_list])
print([len(a_string) for a_string in text_list])
print([a_string for a_string in text_list if len(a_string) >= 3])
