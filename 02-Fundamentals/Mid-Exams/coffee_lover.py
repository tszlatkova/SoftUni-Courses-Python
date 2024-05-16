def include(coffee_list, coffee_type):
    coffee_list.append(coffee_type)

    return coffee_list


def remove(coffee_list, first_last, number_to_remove):
    number = int(number_to_remove)
    if first_last == 'first':
        for _ in range(number):
            coffee_list.pop(0)
    elif first_last == 'last':
        for _ in range(number):
            coffee_list.pop(-1)

    return coffee_list


def switch_places(coffee_list, index1, index2):
    coffee_list[index1], coffee_list[index2] = coffee_list[index2], coffee_list[index1]

    return coffee_list


coffee = input().split(' ')
commands_number = int(input())

for i in range(commands_number):
    command = input().split(' ')

    if command[0] == 'Include':
        coffee = include(coffee, command[1])

    elif command[0] == 'Remove':
        if 0 <= int(command[2]) < len(coffee):
            coffee = remove(coffee, command[1], command[2])

    elif command[0] == 'Prefer':
        if 0 <= int(command[1]) < len(coffee) and 0 <= int(command[2]) < len(coffee):
            coffee = switch_places(coffee, int(command[1]), int(command[2]))

    elif command[0] == 'Reverse':
        coffee.reverse()

print('Coffees:')
print(*coffee)