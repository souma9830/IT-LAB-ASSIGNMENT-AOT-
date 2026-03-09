# Write programs as per following specifications: ''Print the length of the longest string
# in the list of strings str_list. Precondition : the list will contain at least one element.

list = input("Enter the List By separate with space : ").split()
max_len = len(list[0])
for ch in list:
    if len(ch) > max_len:
        max_len = len(ch)
print("The max length is :", max_len)
