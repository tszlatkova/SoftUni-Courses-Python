# Write a program that reads a string with N integers from the console, separated by a
# single space, and reverses them using a stack. Print the reversed integers on one line,
# separated by a single space.

integers = input().split()

reversed_integers = []

for _ in range(len(integers)):
    reversed_integers.append(integers.pop())

print(' '.join(reversed_integers))
