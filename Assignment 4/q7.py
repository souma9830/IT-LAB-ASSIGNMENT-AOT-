# Write a program to compare two equal sized lists and print the first index where they
# differ.

list1=list(map(int,input("Enter the List 1: ").split()))
list2=list(map(int,input("Enter the List 2: ").split()))
for i in range(len(list1)):
    if list1[i]!=list2[i]:
        print("Differ In : ",i)
        break
else:
    print("Both list are identical ")