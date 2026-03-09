# Write a program to implement binary search and linear search as per user choice of
# numbers in a list.

arr = list(map(int, input("Enter the list: ").split()))

key=int(input("Enter the key element:" ))
flag=False
for i in range(len(arr)):
    if(arr[i]==key):
        print("Find the element at ",i)
        flag=True
        break
if(flag==False):
    print("Not present ")


