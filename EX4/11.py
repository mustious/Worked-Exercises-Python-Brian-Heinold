hour = int(input("Enter hour: "))
am_pm = int(input("am (1) or pm(2)? "))
hours_ahead = int(input("How many hours ahead? "))

new_hour = hour + hours_ahead

if (new_hour >= 12) > 0 and am_pm == 1:
    new_am_pm = 2
elif (new_hour >= 12) > 0 and am_pm == 2:
    new_am_pm = 1
else:
    new_am_pm  = am_pm

am_pm_dict = {1: "am", 2: "pm"}

print(f"New hour: {new_hour % 12} {am_pm_dict[new_am_pm]}")