# Write a python program to show the permutation and combination of an inputted List.


def permutation(lst,l,r):
    if l==r:
        print (lst)
    for i in range(l,r):
        lst[l],lst[i]=lst[i],lst[l]
        permutation(lst,l+1,r)
        lst[l],lst[i]=lst[i],lst[l]



lst=(input("Enter the Number ").split())
r=int(input("Enter the value of r: "))
print(permutation(lst,0,len(lst)))