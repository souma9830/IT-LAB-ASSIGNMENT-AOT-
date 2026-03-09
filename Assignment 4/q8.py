# Write a program to reverse a list without using another list or in-built function.

num=list(map(int,input("Enter a list: ").split()))
n=len(num)
for i in range(n//2):
    temp=num[i]
    num[i]=num[n-i-1]
    num[n-i-1]=temp

print(num)