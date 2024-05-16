# Wolves have been reintroduced to Great Britain. You are a sheep farmer and are now plagued by wolves
# who pretend to be sheep. Fortunately, you are good at spotting them.
# Warn the sheep in front of the wolf that it is about to be eaten. Remember that you are standing at the
# front of the queue, which is at the end of the list:
# [sheep, sheep, wolf, sheep, sheep] (YOU ARE HERE AT THE FRONT OF THE QUEUE)
#    4      3            2      1
# If the wolf is the closest animal to you, print "Please go away and stop eating my sheep". Otherwise,
# return "Oi! Sheep number N! You are about to be eaten by a wolf!" where N is the sheep's position in the queue.
# Note: there will always be exactly one wolf on the list.
# Input
# The input will be a single string containing the animals separated by a comma and a single space ", "

input_line= input()

input_queue = input_line.split(', ')

if input_queue[len(input_queue)-1] == 'wolf':
    print('Please go away and stop eating my sheep')
else:
    count = 1
    for animal in range(len(input_queue) - 2, -1, -1):
        if input_queue[animal] == 'wolf':
            print(f'Oi! Sheep number {count}! You are about to be eaten by a wolf!')
            break

        count += 1