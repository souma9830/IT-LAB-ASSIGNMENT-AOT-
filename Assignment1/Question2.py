# Write a program to calculate the amount payable after simple and compound interest.
# Simple Interest = (P ⋆ t ⋆ r) / 100
# Compound Interest = P ⋆ ((1 + r / 100)t - 1)

amount=int(input("Enter The Amount: "))
time=int(input("Enter The Time : "))
rate=int(input("Enter The Interest Rate: "))
simple_interest=(amount*time*rate)/100
compound_interest=amount* ((1+rate/100)**time-1)
print(f"Simple Interest {simple_interest}")
print(f"Compound Interest {compound_interest}")