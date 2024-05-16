# Using comprehension, write a program that receives a text and removes all its vowels, case insensitive. Print the new
# text string after removing the vowels. The vowels that should be considered are 'a', 'o', 'u', 'e', 'i'.

input_text = input()

vows = ['a', 'o', 'u', 'e', 'i']

text_without_vows = [input_text[i] for i in range(len(input_text)) if input_text[i].lower() not in vows]

print(''.join(text_without_vows))