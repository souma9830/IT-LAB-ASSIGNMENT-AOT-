# Create the following lists using a for loop:
# The list ['a','bb','ccc','dddd', . . . ] that ends with 26 copies of the letter z.

lst=[]
for i in range(26):
    ch=chr(97+i)
    lst.append(ch*(i+1))
print(lst)