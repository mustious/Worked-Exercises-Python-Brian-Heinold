import random

countries = ["nigeria", "canada", "japan", "china", "romania", "egypt"]

random_country = random.choice(countries)
len_country = len(random_country)
prediction_list = ["-"] * len_country
current_prediction = "".join(prediction_list)

print("Try guessing what country I chose")
wrong_guesses = 0
already_selected = []

while current_prediction != random_country:
    if wrong_guesses == 5:
        print("You entered 5 wrong guesses. Game over")
        sys.exit()
    guess = input("Guess a letter: ")

    if (guess in random_country) and (guess not in already_selected):
        print("Yes correct, keep trying {}".format(guess))
        already_selected.append(guess)
    elif (guess in random_country) and (guess in already_selected):
        print("You've selected the letter already, try another!")
        continue
    else:
        wrong_guesses += 1
        print("Wrong guess!. {} more wrong guesses and Gameover".format(5 - wrong_guesses))
        continue
    guess_indices = [num for num in range(len_country) if guess == random_country[num]]
    
    for idx in guess_indices:
        prediction_list[idx] = guess

    current_prediction = "".join(prediction_list)
    
    print("The country is based on your guesses: {}".format(current_prediction))

print("You win bro")