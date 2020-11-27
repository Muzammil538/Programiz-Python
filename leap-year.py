#If the year is divisible by 400 then the year is Leap year

year = int(input("Enter the Year: "))

if (year % 400) == 0 or (year % 4) == 0 or (year % 100) == 0:
    print("{0} is a leap year".format(year))
else:
    print("{0} is not a leap year".format(year))
