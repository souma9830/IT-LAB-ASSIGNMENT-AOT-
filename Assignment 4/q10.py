# Write a program to find the arithmetic mean, variance and standard deviation of any
# values in a list.

import math
num=list(map(int,input("Enter the Number : ").split()))
n=len(num)
mean=sum(num)/n

var_sum=0
for x in num:
    var_sum=var_sum+(x-mean)**2

varience=var_sum/n
std_dev=math.sqrt(varience)
print("Mean:", mean)
print("Variance:", varience)
print("Standard Deviation:", std_dev)