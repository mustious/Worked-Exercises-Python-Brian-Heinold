import sys

length_cm = float(input("Please enter length in centimeters: "))

cm_to_inches = 1/2.54
if length_cm < 0:
    print("Invalid entry")
    sys.exit()
else:
    length_inches = length_cm * cm_to_inches
    print("THe length in inches is {:.2f}".format(length_inches))
