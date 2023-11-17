# Write a program that reads a string from the console that contains:
# •	Explosions marked with '>'
# •	Immediately after the mark, there will be an integer x, which signifies the strength of the explosion
# •	Any other characters
# Your task is to delete x characters, starting after the exploded character ('>'). If you find another explosion
# mark ('>') while deleting characters, you should add the strength to your previous explosion. You should not delete
# the explosion character – '>'.
# When all characters are processed, print the final string.
# Constraints
# •	You will always receive strength for the explosions
# •	The path will consist only of letters from the Latin alphabet, integers, and the char '>'
# •	The strength of the punches will be in the interval [0…9]

text = input()
output_text = ''
strength = 0

for index in range(len(text)):

    if strength > 0 and text[index] != '>':
        strength -= 1
    elif text[index] == '>':
        output_text += text[index]
        strength += int(text[index + 1])
    else:
        output_text += text[index]

print(output_text)