# Tom is working at the supermarket, and he needs your help to keep track of his clients.
# Write a program that reads lines of input consisting of a customer's name and adds it to
# the end of a queue until "End" is received. If, in the meantime, you receive the command
# "Paid", you should print each customer in the order they are served (from the first to
# the last one) and empty the queue.
#
# When you receive "End", you should print the count of the remaining people in the queue
# in the format: "{count} people remaining.".

from collections import deque

que_customers = deque([])
name_customer = input()

while name_customer != 'End':

    if name_customer != 'Paid':
        que_customers.append(name_customer)
    else:
        for i in range(len(que_customers)):
            print(que_customers[i])

        que_customers = deque([])

    name_customer = input()

print(f'{len(que_customers)} people remaining.')

# Better solution instead of "for"

# while queue:
#     print(que_customers.popleft())
