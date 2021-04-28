number = float(input("Please enter the number you want to calculate it's square root? "))

previous_guess = number
current_guess = 1.0

while abs(previous_guess - current_guess) > 10 ** -10:
    print(current_guess)
    new_solution = (current_guess + (number/current_guess))/2
    previous_guess = current_guess
    current_guess = new_solution

print("The square root of {} is {}".format(number, current_guess))