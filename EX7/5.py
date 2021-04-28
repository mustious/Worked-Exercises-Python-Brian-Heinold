print("enter a list of numbers seperated by space e.g hello how coming soon")
text_input = input("Enter your strings here: ")
text_list = text_input.split()
new_text = [text[1:] for text in text_list]
print(new_text)
