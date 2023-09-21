# Write a function that receives 3 characters. Concatenate all the characters into one string and print it on the
# console.

concatenate_string = ''

for i in range(0,3):
    string_to_add = input()
    concatenate_string += string_to_add

print(concatenate_string)