hour = int(input("Enter hour: "))
enter_hour = int(input("How many hours ahead? "))
print(f"New hour: {(hour + enter_hour) % 12} o'clock")
