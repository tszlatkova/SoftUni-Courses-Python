# You will be given a sequence consisting of parentheses. Your job is to determine whether
# the expression is balanced. A sequence of parentheses is balanced if every opening
# parenthesis has a corresponding closing parenthesis that occurs after the former. There
# will be no interval symbols between the parentheses. You will be given three types of
# parentheses: (), {}, and [].
# {[()]} - Parentheses are balanced.
# (){}[] - Parentheses are balanced.
# {[(])} - Parentheses are NOT balanced.

# Input
# •	On a single line, you will receive a sequence of parentheses.

# Output
# •	For each test case, print on a new line "YES" if the parentheses are balanced.
# •	Otherwise, print "NO"

# Constraints
# •	1 ≤ lens ≤ 1000, where the lens is the length of the sequence
# •	Each character of the sequence will be one of {, }, (, ), [, ]

sequence_parentheses = [char for char in input()]
opening_brackets = []
balanced = True

for i in range(len(sequence_parentheses)):
    if sequence_parentheses[0] in ['}', ')', ']']:
        balanced = False
        break

    current_parenthesis = sequence_parentheses[i]

    if current_parenthesis in ['{', '(', '[']:
        opening_brackets.append(current_parenthesis)

    elif current_parenthesis in ['}', ')', ']']:
        if len(opening_brackets) > 0:
            opening_parenthesis = opening_brackets.pop()
            closing_parenthesis = current_parenthesis

            if opening_parenthesis + closing_parenthesis in ['()', '{}', '[]']:
                continue
            else:
                balanced = False
                break
        else:
            balanced = False
            break

if balanced and len(opening_brackets) == 0:
    print('YES')
else:
    print('NO')
