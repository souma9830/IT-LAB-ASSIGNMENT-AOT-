# Write a program to take a 2-digit number and then print the reversed number. That is, if
# the input given is 25, the program should print 52. Then extend it for 3-digit number and
# also check for odd and even.
number =int (input("Enter a Number : "))
# print("Reverse Number is ", number[::-1]) #this is the shortest method 
rev=0
while number>0:
    digit=number%10
    rev=rev*10+digit
    number=number//10

print("The Result is : ",rev)
if(rev%2==0):
    print("The number is Even")
else:
    print("Number is Odd")