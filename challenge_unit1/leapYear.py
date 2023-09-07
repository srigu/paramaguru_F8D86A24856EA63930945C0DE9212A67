def LeapYear(year):
    if year%4==0 and 100!=0:
        print(year,"is a leap year")
    elif year%400==0:
        print(year,"is a leap year")
    else:
        print(year,"is a not a leap year")
year=int(input("Enter a year:"))        
LeapYear(year)
        
