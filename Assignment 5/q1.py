# Write a Python function that takes a list and returns a new list with unique elements of
# the first list.
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]


def unique_list(num):
    newlist=[]
    for x in num:
        if x not in newlist:
            newlist.append(x)
    return newlist

num=list(map(int,input("Enter the List: ").split()))
result=unique_list(num)
print(result)