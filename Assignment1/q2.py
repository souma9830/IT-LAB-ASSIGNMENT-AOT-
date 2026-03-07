# Write a program to calculate the amount payable after simple and compound interest.
# Simple Interest = (P ⋆ t ⋆ r) / 100
# Compound Interest = P ⋆ ((1 + r / 100)t - 1)

p = float(input("Enter The Principle: "))
t = float(input("Enter the time: "))
r = float(input("Enter the Interest rate in percentage: "))
simple_interest = (p*t*r)/100
total_si=simple_interest+p
compound_interest = p*((1+r/100)**t-1)
total_com=compound_interest+p
print("Simple Interest is : ", simple_interest)
print("Total after Simple Interest: ",total_si)
print("Compound Interest is : ", compound_interest)
print("Total after Compound Interest: ",total_com)
