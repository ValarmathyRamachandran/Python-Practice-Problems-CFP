def leap_year_function():
    input_year = input("Enter any Year :: ")
    year = int(input_year)
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print("Specified year is a leap year")
    else:
        print("Specified year is not a leap year")


leap_year_function()
