user_year = int(input("Enter your year: "))
init_year = 1600

no_leap = 0
leap_years = []
for year in range(init_year, user_year + 1, 4):
    if year % 100 != 0:
        no_leap += 1
        leap_years.append(year)

    else:
        if (year // 100) / 4 == 0:
            no_leap += 1
            leap_years.append(year)

print(no_leap)
print(leap_years)