# Reduce a string of lowercase characters in range ascii [‘a’..’z’] by doing a series of
# operations. In each operation, select a pair of adjacent letters that match, and delete them.
# Delete as many characters as possible using this method and return the resulting string. If
# the final string is empty, return Empty String

string=input("Enter the String: ")
stack=[]
for ch in string:
    if stack and stack[-1]==ch:
        stack.pop()
    else:
        stack.append(ch)

result="".join(stack)
if(result==""):
    print("Empty String")
else:
    print(result)