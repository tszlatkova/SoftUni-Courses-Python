# Beaches are filled with sand, water, fish, and sun. Given a string, calculate how many times the words "Sand",
# "Water", "Fish", and "Sun" appear (case insensitive).

input_line = input()
input_line_lower = input_line.lower()

beach_words = ['sand', 'water', 'fish', 'sun']

count = 0

for word in range(0, 4):
        count += input_line_lower.count(beach_words[word])

print(count)

# NOT GOOD!
# If it appears more than one time it doesn't count it
# count = 0
#
# for word in range(0, 4):
#     if beach_words[word] in input_line_lower:
#         count += 1
#
# print(count)