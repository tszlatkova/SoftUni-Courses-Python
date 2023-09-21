# Напишете програма, която да принтира на конзолата всички комбинации от 3 букви в зададен интервал, като се пропускат
# комбинациите съдържащи зададена от конзолата буква. Накрая трябва да се изпринтира броят на отпечатаните комбинации.
# Вход
# Входът се чете от конзолата и съдържа точно 3 реда:
# Ред 1.	Малка буква от английската азбука за начало на интервала – от ‘a’ до ‚z’.
# Ред 2.	Малка буква от английската азбука за край на интервала  – от първата буква до ‚z’.
# Ред 3.	Малка буква от английската азбука – от ‘a’ до ‚z’ – като комбинациите съдържащи тази буквата се пропускат.
# Изход
# Да се отпечатат на един ред всички комбинации отговарящи на условието плюс броят им разделени с интервал.

# print(ord('a'))

start_letter = input()
end_letter = input()
skip_letter = input()

skip_letter_in_number = ord(skip_letter)
count_combinations = 0

for x in range(ord(start_letter), ord(end_letter)+1):
    for y in range(ord(start_letter), ord(end_letter)+1):
        for z in range(ord(start_letter), ord(end_letter)+1):
            if x != skip_letter_in_number and y != skip_letter_in_number and z != skip_letter_in_number:
                count_combinations += 1
                print(f'{chr(x)}{chr(y)}{chr(z)}', end = ' ')

print(count_combinations)