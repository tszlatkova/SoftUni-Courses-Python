# Write a function that, depending on the first line of the input, reads one of the following strings: "int",
# "real", or "string".
# •	If the data type is an int, multiply the number by 2.
# •	If the data type is real, multiply the number by 1.5 and format the result to the second decimal point.
# •	If the data type is a string, surround the input with "$".
# Print the result on the console.

def data_type(input1, input2):
    if input1 == 'int':
        return int(input2) * 2
    elif input1 == 'real':
        return f'{float(input2) * 1.50:.2f}'
    elif input1 == 'string':
        return '$' + input2 + '$'


input_line1 = input()
input_line2 = input()

print(data_type(input_line1, input_line2))