# Напишете програма, която чете от конзолата цели числа, докато не се получи команда "stop". Да се намери сумата на
# всички въведени прости и сумата на всички въведени непрости числа. Тъй като по дефиниция от математиката
# отрицателните числа не могат да бъдат прости, ако на входа се подаде отрицателно число, да се изведе следното
# съобщение "Number is negative.". В този случай въведено число се игнорира и не се прибавя към нито една от двете суми,
# а програмата продължава своето изпълнение, очаквайки въвеждане на следващо число.
# На изхода да се отпечатат на два реда двете намерени суми в следния формат:
# •	"Sum of all prime numbers is: {prime numbers sum}"
# •	"Sum of all non prime numbers is: {nonprime numbers sum}"

input_line = input()

sum_prime = 0
sum_nonprime = 0
not_prime = False

while input_line != 'stop':
    number = int(input_line)

    if number < 0:
        print(f'Number is negative.')
        input_line = input()
        continue
    elif number == 0:
        not_prime = True
    elif number == 1 or number == 2:
        not_prime = False
    else:
        for num in range(2, number):
            if number % num == 0:
                not_prime = True
                break

    if not_prime:
        sum_nonprime += number
        not_prime = False
    else:
        sum_prime += number

    input_line = input()

print(f'Sum of all prime numbers is: {sum_prime}')
print(f'Sum of all non prime numbers is: {sum_nonprime}')