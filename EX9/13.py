"""
rock paper scissors program between player and computer
"""
import random

rounds = 5
print("Use the following numbers: \n1, 2, 3 for rock, paper and scissors respectively")

selecion_dict = {1: "rock", 2: "paper", 3: "scissors"}

total_player_score = 0
total_computer_score = 0
for round in range(rounds):
    print("Round {}".format(round+1))
    
    # current scores
    player_score = 0
    computer_score = 0

    user_choice = int(input("User select an object: "))
    print("You choose - {}".format(selecion_dict[user_choice]))
    computer_choice = random.choice([1, 2, 3])
    print("Computer choose - {}".format(selecion_dict[computer_choice]))
    
    # game rules
    if user_choice == computer_choice:
        print("It's a tie")
    elif user_choice == 1 and computer_choice == 2:
        print("Computer Wins!")
        computer_score += 1
    elif user_choice == 2 and computer_choice == 1:
        print("Player Wins!")
        player_score += 1
    elif user_choice == 3 and computer_choice == 1:
        print("Computer Wins!")
        computer_score += 1
    elif user_choice == 1 and computer_choice == 3:
        print("Player Wins!")
        player_score += 1
    elif user_choice == 2 and computer_choice == 3:
        print("Computer Wins!")
        computer_score += 1
    elif user_choice == 3 and computer_choice == 2:
        print("Player Wins!")
        player_score += 1

    total_computer_score += computer_score
    total_player_score += player_score

    if (total_computer_score >= 3) or (total_player_score >= 3):
        break
    
if total_player_score > total_computer_score:
    print("Player Wins the with {} games".format(total_player_score))
elif total_player_score < total_computer_score:
    print("Computer Wins the with {} games".format(total_computer_score))