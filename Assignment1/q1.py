# Write a program that asks the number of years as input, and then prints out the number
# of days, hours, minutes, and seconds in that number of years. Assume 365 days per year
# and also check that year for leap year or not.

years = int(input("Enter The Number of Years"))
total_day = 0
for i in range(1, years+1):
    year = int(input(f"Enter {i} year for checking leap year"))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("It is a Leap Year")
        total_day += 366
    else:
        print("It is not a leap year")
        total_day += 365
hours = total_day*24
minutes = hours*60
second = minutes*60
print("\nTotal Days: ", total_day)
print("Total Hours: ", hours)
print("Total Min: ", minutes)
print("Total second: ", second)
