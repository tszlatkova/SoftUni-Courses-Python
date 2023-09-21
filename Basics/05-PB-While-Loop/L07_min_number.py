# Напишете програма, която до получаване на командата "Stop", чете цели числа, въведени от потребителя,
# намира най-малкото измежду тях и го принтира. Въвежда се по едно число на ред.

user_input = input()
min_number = int(user_input)

while user_input != 'Stop':
    user_input = int(user_input)

    if user_input < min_number:
        min_number = user_input

    user_input = input()

else:
    print(min_number)