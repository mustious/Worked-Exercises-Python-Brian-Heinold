text = input("Enter text here: ")
search_words = ["a", "an", "the"]

count = 0
for word in text.strip().split():
    if word in search_words:
        count += 1
print("The number of search words is {}".format(count))
