start_year = int(input("Enter the Start Year: "))
end_year = int(input("Enter the End Year: "))

leap_years = []
for year in range(start_year, end_year + 1):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap_years.append(year)
        else:
            leap_years.append(year)

print("Leap years between", start_year, "and", end_year, "are:")
print(leap_years)
print("Total:", len(leap_years), "leap years")