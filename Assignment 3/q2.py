# Write a Python function that accepts a string and calculates the number of uppercase
# letters
# and lowercase letters.
def count_case(text):
    lower=0
    upper=0
    for ch in text:
        if ch.isupper():
            upper+=1
        elif ch.islower():
            lower+=1
    print("Upper Letter: ",upper)
    print("Lower Letter: ",lower)
text=input("Enter a Word: ")
count_case(text)