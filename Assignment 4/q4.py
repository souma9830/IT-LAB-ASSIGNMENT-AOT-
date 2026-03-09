# Write a program to read two lists num and denum which contain the numerators and
# denominators of the same fractions at the respective indexes. Then display the
# smallest and largest fraction along with its index.

numerator=list(map(int,input("Enter The Numerator: ").split()))
denominator=list(map(int,input("Enter The denominator: ").split()))
list=[]
for i in range(len(numerator)):
    list.append(numerator[i]/denominator[i])
min_val=list[0]
max_val=list[0]
min_idx=0
max_idx=0
for i in range(len(list)):
    if min_val>list[i]:
        min_val=list[i]
        min_idx=i
    elif max_val<list[i]:
        max_val=list[i]
        max_idx=i
print("The min val in the list is :",min_val,"at index: ",min_idx)
print("The max val is ",max_val,"at index: ",max_idx)