decimal=int(input("enter the decimal number: "))
binary=""
while decimal>0:
    reaminder=decimal%2
    binary=str(reaminder)+binary
    decimal=decimal//2
print(binary)