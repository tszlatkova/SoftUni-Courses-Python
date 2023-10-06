# Create a function that receives three parameters, calculates a result depending on the given operator, and returns
# it. Print the result of the function. The input comes as three parameters – an operator as a string and two integer
# numbers. The operator can be one of the following:  "multiply", "divide", "add", "subtract".

def calculate(operator: str, first_int: int, second_int: int):
    if operator == 'multiply':
        return first_int * second_int
    elif operator == 'divide':
        return int(first_int / second_int)
    elif operator == 'add':
        return first_int + second_int
    elif operator == 'subtract':
        return first_int - second_int


operation = input()
first_number = int(input())
second_number = int(input())

result = calculate(operation, first_number, second_number)

print(result)