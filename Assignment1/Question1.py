# Write a program that asks the number of years as input, and then prints out the number
# of days, hours, minutes, and seconds in that number of years. Assume 365 days per year
# and also check that year for leap year or not.

years=int(input("Enter The Number Of year: "))
total_days=0
for i in range(1,years+1):
    year=int(input(f"Enter year {i} : "))
    if(year%400==0) or (year%4==0 and year%100!=0):
        print(f"{year} is Leap Year.")
        total_days+=366
    else:
        print(f"{year} is not a Leap Year.")
        total_days+=365


hours=total_days*24
minutes=hours*60
second=minutes*60
print("Here Is The Data ")
print(f"Total Number Of days in this {years} years: {total_days}")
print(f"Total Hour is {hours}")
print(f"Total minutes : {minutes}")
print(f"Total second {second}")