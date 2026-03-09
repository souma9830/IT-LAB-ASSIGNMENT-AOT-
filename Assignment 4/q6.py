# Write a program to move all duplicate values in a list to the end of the list.
word=list(map(int,input("Enter the string: ").split()))
unique=[]
dublicate=[]
for i in word:
    if i not in unique:
        unique.append(i)
    else:
        dublicate.append(i)

result=unique+dublicate
print(result)