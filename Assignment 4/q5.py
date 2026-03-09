# Write a program to display the maximum and minimum values from the specified
# range of indices of the list

num = list(map(int, input("Enter the List: ").split()))
start = int(input("Enter the Starting index: "))
end = int(input("Enter the Ending index: "))
min_val = num[start]
max_val = num[start]
for i in range(start, end+1):
    if (min_val < num[i]):
        min_val = num[i]
    else:
        max_val = num[i]

print("Minimum value:", min_val)
print("Maximum value:", max_val)
