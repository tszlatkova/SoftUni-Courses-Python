# Напишете програма, която чете цяло число от конзолата и на всеки следващ ред цели числа, докато тяхната сума
# стане по-голяма или равна на първоначалното число. След приключване на четенето да се отпечата сумата на
# въведените числа.

number = int(input())
sum_numbers = 0

while True:
    new_number = int(input())
    sum_numbers += new_number

    if sum_numbers >= number:
        print(sum_numbers)
        break