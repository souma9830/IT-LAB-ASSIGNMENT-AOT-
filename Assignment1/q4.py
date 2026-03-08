# Say a box of cookies can hold 24 cookies, and a container can hold 75 boxes of cookies.
# Write a program that prompts the user to enter the total number of cookies, then outputs
# the number of boxes and the number of containers to ship the cookies. Note that each
# box must contain the specified number of cookies, and each container must contain the
# specified number of boxes. If the last box of cookies contains less than the number of
# specified cookies, you can discard it and output the number of leftover cookies. Similarly,
# if the last container contains less than the number of specified boxes, you can discard it
# and output the number of leftover boxes.

total_cookie=int(input("Enter The total Number Of Cookie: "))
box=total_cookie//24
leftover_cookie=total_cookie%24
container=box//75
leftover_box=box%75
print("Total Number Of Box Need: ",box)
print("Leftover boxes: ",leftover_cookie)
print("Total Number of container: ",container)
print("Total container Leftover: ",leftover_box)