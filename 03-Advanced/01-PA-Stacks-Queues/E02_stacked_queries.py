# You have an empty stack. You will receive an integer – N. On the following N lines, you
# will receive queries. Each query is one of these four types:
# •	'1 {number}' – push the number (integer) into the stack
# •	'2' – delete the number at the top of the stack
# •	'3' – print the maximum number in the stack
# •	'4' – print the minimum number in the stack
# It is guaranteed that each query is valid.
# After you go through all the queries, print the stack from top to bottom in the
# following format:
# "{n}, {n1}, {n2}, ... {nn}"

# n = int(input())
#
# my_stack = []
#
# for _ in range(n):
#     query = input()
#
#     if '1' in query:
#         _, number_to_push = query.split()
#         my_stack.append(int(number_to_push))
#     elif '2' in query and len(my_stack) >= 1:
#         my_stack.pop()
#     elif '3' in query:
#         print(max(my_stack))
#     elif '4' in query:
#         print(min(my_stack))
#
# my_stack.reverse()
#
# print(*my_stack, sep=', ')

n = int(input())

my_stack = []

for _ in range(n):
    query = input().split()

    if query[0] == '1':
        my_stack.append(int(query[1]))
    elif query[0] == '2' and len(my_stack) >= 1:
        my_stack.pop()
    elif query[0] == '3' and len(my_stack) >= 1:
        print(max(my_stack))
    elif query[0] == '4' and len(my_stack) >= 1:
        print(min(my_stack))

my_stack.reverse()

print(*my_stack, sep=', ')
