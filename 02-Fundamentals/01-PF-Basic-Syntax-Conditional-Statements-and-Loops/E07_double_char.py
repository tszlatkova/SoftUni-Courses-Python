# You will be given strings until you receive the command "End". For each string given, you should print a
# string in which each character (case-sensitive) is repeated twice. Note that if you receive the string "SoftUni",
# you should NOT print it!

input_line = input()

while input_line != 'End':
    if input_line == 'SoftUni':
        input_line = input()
        continue
    else:
        double_word = ''
        for letter in range(0, len(input_line)):
            double_word += 2 * input_line[letter]

    print(double_word)
    input_line = input()