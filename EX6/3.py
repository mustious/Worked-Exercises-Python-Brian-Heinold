formula_text = input("enter your fomula: ")

left_bracket_count = formula_text.count("(")
right_bracket_count = formula_text.count(")")

if left_bracket_count == right_bracket_count:
    print("Same number of opening and closing braces")
else:
    print("Unequal number of braces")