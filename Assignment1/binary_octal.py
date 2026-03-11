binary = input("Enter the Binary Number: ")
decimal = 0
power = 0
for digit in binary[::-1]:
    decimal = decimal+int(digit)*(2**power)
    power += 1
print(decimal)

octal = ""
while decimal > 0:
    remainder = decimal % 8
    octal = str(remainder)+octal
    decimal = decimal//8
print(octal)
