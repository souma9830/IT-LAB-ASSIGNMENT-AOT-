# Write a program to check whether a user input string is palindrome or not.

def palindrom(text):
    rev = ""
    for ch in text:
        rev = ch+rev
    if (text == rev):
        print("Palindorm")
    else:
        print("Not Palindorme")


text = input("Enter a word: ")
palindrom(text)

# 2nd method


text = input("Enter a word: ")
    
if text == text[::-1]:
        print("Palindrom")
else:
        print("Not Palindrom")
