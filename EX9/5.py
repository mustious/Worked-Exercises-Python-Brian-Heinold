count_A = 0
test_scores = []

print("Enter a negative number to show end of input")
while True:
    test_score = int(input("Enter your score: "))
    if test_score < -1:
        break
    elif test_score >= 90:
        count_A += 1
    test_scores.append(test_score)

print("You have {} As".format(count_A))
print("Your average score is {:.2f}".format(sum(test_scores)/len(test_scores)))
