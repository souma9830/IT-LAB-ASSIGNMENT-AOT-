# In the Byteland country, a string S is said to super ASCII string if and only if the count of
# each character in the string is equal to its ASCII value. In the Byteland country ASCII code of
# ‘a’ is 1,
# ‘b’ is 2, …, ‘z’ is 26. The task is to find out whether the given string is a super ASCII string or
# not.
# If true, then print “Yes” otherwise print “No”.


s=input("Enter a Word: ")
flag=True
for ch in set(s):
    count=s.count(ch)
    ascii_code=ord(ch)-96

    if(count!=ascii_code):
        flag=False
        break
if flag:
    print("Yes")
else:
    print("NO")
