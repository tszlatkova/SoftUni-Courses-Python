# Write a program that keeps all the unique chemical elements. On the first line, you will
# be given a number n - the count of input lines that you will receive. On the following n
# lines, you will be receiving chemical compounds separated by a single space. Your task
# is to print all the unique ones on separate lines (the order does not matter):

number_lines = int(input())
chemical_compounds = set()

for _ in range(number_lines):
    chemicals_to_add = [chemical for chemical in input().split(' ')]

    for chemical in chemicals_to_add:
        chemical_compounds.add(chemical)

    # for el in input().split():
    #     chemical_compounds.add(el)

print(*chemical_compounds, sep='\n')
