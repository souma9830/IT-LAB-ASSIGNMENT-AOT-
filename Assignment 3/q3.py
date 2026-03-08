# Write a Python function to check whether a string is a pangram or not.
# Note : Pangrams are words or sentences containing every letter of the alphabet at least
# once.

def panagram(sen):
    sen = sen.lower()
    letter = "abcdefghijklmnopqrstuvwxyz"
    for ch in letter:
        if ch not in sen:
            return "Not Panagram"

    return "panagram"


sentence = input("Enter a Sentence: ")
print(panagram(sentence))
