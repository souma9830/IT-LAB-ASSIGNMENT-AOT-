
s1 = float(input("Enter marks of subject 1: "))
s2 = float(input("Enter marks of subject 2: "))
s3 = float(input("Enter marks of subject 3: "))
s4 = float(input("Enter marks of subject 4: "))
s5 = float(input("Enter marks of subject 5: "))

# Calculate average
avg = (s1 + s2 + s3 + s4 + s5) / 5

# Determine grade
if avg >= 91 and avg <= 100:
    grade = "O"
elif avg >= 81:
    grade = "E"
elif avg >= 71:
    grade = "A"
elif avg >= 61:
    grade = "B"
elif avg >= 51:
    grade = "C"
elif avg >= 41:
    grade = "D"
else:
    grade = "F"

print("Average Marks:", avg)
print("Grade:", grade)