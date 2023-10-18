# Write a program that receives a sequence of numbers (a string containing integers separated by ", ") and prints the
# numbers sorted into lists of 10's in the format "Group of {group}'s: {list_of_numbers}".

# Examples:
# •	The numbers 2, 8, 4, and 10 fall into the group of 10's.
# •	The numbers 13, 19, 14, and 15 fall into the group of 20's.
# For more clarification, see the examples below.

def remove_sublist(list_numbers, sublist_numbers):
    modified_list = []

    for i in range(len(list_numbers)):
        if list_numbers[i] not in sublist_numbers:
            modified_list.append(list_numbers[i])

    return modified_list


def max_group(list_numbers):
    max_element = max(list_numbers)

    if max_element % 10 == 0:
        return max_element // 10
    else:
        return max_element // 10 + 1


numbers = [int(i) for i in input().split(', ')]

final_group = max_group(numbers)

for i in range(1, final_group + 1):
    group_list = []
    current_group = i * 10

    for j in range(len(numbers)):
        if numbers[j] <= current_group:
            group_list.append(numbers[j])

    numbers = remove_sublist(numbers, group_list)

    print(f"Group of {current_group}'s: {group_list}")