# Write a regular expression to match a valid phone number from Sofia. After you find all valid phones, print them on
# the console, separated by a comma and a space ", ". The input will be a string containing phone numbers and other
# symbols.

# Compose the Regular Expression
# A valid number has the following characteristics:
# •	It starts with "+359"
# •	Then, it is followed by the area code (always 2)
# •	After that, it is followed by a number:
# o	The number consists of 7 digits (separated into two groups of 3 and 4 digits, respectively).
# •	The different parts are separated by either a space (' ') or a hyphen ('-').

# You can use the following RegEx properties to help with the matching:
# •	Use quantifiers to match a specific number of digits
# •	Use a capturing group to make sure the delimiter is only one of the allowed characters (space or hyphen) and not a
# combination of both (e.g., +359 2-111 111 has mixed delimiters, it is invalid). Use a group backreference to achieve
# this.
# •	Add a word boundary at the end of the match to avoid partial matches.
# •	Ensure that there is a space before the '+' sign, or it is positioned at the beginning of the string.
# You can use the following table of values to test your RegEx:
# Match ALL of these                                   	Match NONE of these
# +359 2 222 2222
# +359-2-222-2222	                       359-2-222-2222, +359/2/222/2222, +359-2 222 2222
#                                          +359 2-222-2222, +359-2-222-222, +359-2-222-22222

import re

phone_numbers = input()
pattern = '\+359 2 \d{3} \d{4}\\b|\+359-2-\d{3}-\d{4}\\b'

valid_phone_numbers = re.findall(pattern, phone_numbers)

print(', '.join(valid_phone_numbers))
