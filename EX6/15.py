my_class = input("Enter a college class: ")
adjective = input("Enter an adjective: ")
activity = input("Enter an activity: ")

full_text = "{} class is was really {} today. We learned how to play {} today in class. "\
    "I can't wait for tomorrow's class".format(my_class.upper(), adjective.upper(), activity.upper())
print(full_text)
