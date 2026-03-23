## run python reverse_string.py

# string = input('Input String : ')
# reverse_string = ''
# result = ''
# index = len(string) - 1


# while index >= 0:
#     result = string[index]
#     reverse_string = reverse_string + result
#     index = index - 1

# print(reverse_string)

######################################################

string = input('Input String : ')
reverse_string = ''


for char in string:
    reverse_string = char + reverse_string 

print('Reversed String :', reverse_string)

#######################################################

# string = input(" Input string : ")
# reverse_string = ''

# for char in string:
#     reverse_string = char + reverse_string

# print(reverse_string)

###########################################################

# string = input(' Input string : ')
# string_list = list(string)
# reverse_string = ''
# start = 0
# end = len(string) - 1

# while (start < end):
#     string_list[start] , string_list[end] = string_list[end] , string_list[start]
#     start += 1
#     end -= 1

# reverse_string = "".join(string_list)
# print(reverse_string)


###########################################################

# s = ["t","e","a","m"]

# start = 0
# end = len(s) - 1

# while (start < end):
#     s[start] , s[end] = s[end] , s[start]
#     start += 1
#     end -= 1


# reverse_string = ''.join(s)
# print(reverse_string)