# On the first line, you will receive n – the number of lines, which will follow. On the following n lines, you
# will receive one of the following:
# •	Opening bracket – "(",
# •	Closing bracket – ")" or
# •	Random string
# Your task is to find out if the brackets are balanced. That means after every opening bracket should follow a closing
# one. Nested parentheses are not valid, and if, for example, two consecutive opening brackets exist, the expression
# should be marked as unbalanced. You should print "BALANCED" if the parentheses are balanced and "UNBALANCED"
# otherwise.

lines = int(input())

opening_bracket = 0
balanced = False

for i in range(1, lines + 1):
    input_line = input()

    if input_line == '(':
        opening_bracket += 1

        if opening_bracket > 1:
            balanced = False
            break
    elif input_line == ')' and opening_bracket == 0:
        balanced = False
        break
    elif input_line == ')':
        balanced = True
        opening_bracket = 0

if balanced:
    print('BALANCED')
else:
    print('UNBALANCED')