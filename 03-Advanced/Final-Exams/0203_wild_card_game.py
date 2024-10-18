# Write a function named draw_cards that takes a variable number of arguments (tuples)
# and keyword arguments (key-value pairs).
# The function receives information about monster cards and spell cards and returns a
# formatted string.
# The arguments will be passed as follows:
# •	The first group of arguments will be an unknown number of tuples
# o	the first element in the tuple is the name of the card (string) (every card will have
# a unique name)
# o	the second element is the card type (string) (every card can either have a "monster"
# type or "spell" type)
# •	The second group will be an unknown number of keyword arguments (key-value pairs)
# o	the key is the name of the card (string) (every card will have a unique name)
# o	the value is the card type (string) (every card can either have a "monster" or "spell"
# type)
# After receiving the information and calling the function:
# •	You should keep track of the different card types in separate collections
# •	Sort the monster cards in descending order by their name.
# •	Sort the spell cards in ascending order by their name.
# •	Format the result as follows (each card info on a different line):
# o	Separate monster and spell cards under appropriate headings:
# 	First are the monster cards (only if there are cards from this specific type), each on
# a different line under the heading
# "Monster cards:"
# 	Then the spell cards (only if there are cards from this specific type), each on a
# different line under the heading
# "Spell cards:"
# In the end, return the output as described below.
# Note: Submit only the function in the judge system
# Input
# •	There will be no input from the console, just parameters passed to your function.
# Output
# •	The output should look like this (each string should be on a new line):
# o	Prefix monster names with "  ***" - (exactly two spaces and three asterisks "*").
# o	Prefix spell names with "  $$$" - (exactly two spaces and three dollar signs "$").
#    "Monster cards:"
#    "  ***{monster_name1}"
#    "  ***{monster_name2}"
# ...
#    "  ***{monster_nameN}"
#    "Spell cards:"
#    "  $$${spell_name1}"
#    "  $$${spell_name2}"
# ...
#    "  $$${spell_nameN}"
#
# •	Important notes:
# o	You may exclusively draw either "monster" or "spell" cards. If so, return only the
# type you have. Do not include the heading for the missing card type in your formatted
# string.
# o	There are exactly two intervals before the monster's and the spell's names.
# Constraints
# •	The arguments will be always before the keyword arguments.
# •	Each tuple will always contain the monster's or spell's name with its type.
# •	There always will be at least one tuple and at least one keyword argument with a valid
# name and a valid type. (Valid card types are "monster" and "spell")

def draw_cards(*args, **kwargs):
    monsters = []
    spells = []