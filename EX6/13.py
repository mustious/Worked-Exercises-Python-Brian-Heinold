import sys

print("Enter two strings of the same lenght")
first = input("Enter string 1: ")
second = input("Enter string 2: ")

if len(first) != len(second):
    print("strings are not of the same length")
    sys.exit()

combo = ""
for i in range(len(first)):
    combo += first[i]
    combo += second[i]

print(combo)
        