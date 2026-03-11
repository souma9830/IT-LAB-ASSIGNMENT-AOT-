string=input("Enter a string: ")
max_count=0
max_ch=""
for ch in string:
    count=string.count(ch)
    if count>max_count and max_ch!=" ":
        max_count=count
        max_ch=ch

print(max_ch)
print(max_count)