n = int(input("How many element you want : "))
arr = []
for i in range(n):
    x = int(input())
    arr.append(x)
print(arr)

low = 0
high = n-1
key = int(input("Enter the element you want to find: "))
flag = False
while low <= high:
    mid = low+high//2
    if (arr[mid] == key):
        print("Element found at position: ", mid)
        flag = True
        break
    elif (arr[mid] < key):
        low = mid+1
    else:
        high = mid-1
