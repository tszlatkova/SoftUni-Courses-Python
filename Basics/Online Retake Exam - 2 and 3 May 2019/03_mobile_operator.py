# Мобилен оператор предлага договори с различна месечна такса в зависимост от срока - 1 или 2 години.
# Да се напише програма, която изчислява дължимата сума, която трябва да се плати за определен брой месеци.
# срок / тип	            Small	            Middle          	Large	            ExtraLarge
# 1 година(one)	            9.98 лв.           	18.99 лв.       	25.98 лв.          	35.99 лв.
# 2 години(two)         	8.58 лв.	        17.09 лв.	        23.59 лв.	        31.79 лв.
# Условия:
# •	при добавен мобилен интернет, към таксата за един месец се добавя:
# o	при такса по-малка или равна на 10.00 лв.  5.50 лв.
# o	при такса по-малка или равна на 30.00 лв.  4.35 лв.
# o	при такса по-голяма от 30.00 лв.  3.85 лв.
# •	ако договорът e за две години, общата сума се намалява с 3.75%
# Вход
# От конзолата се четат 3 реда:
# 1.	Срок на договор – текст – "one", или "two"
# 2.	Тип на договор – текст – "Small",  "Middle", "Large"или "ExtraLarge"
# 3.	Добавен мобилен интернет – текст – "yes" или "no"
# 4.	Брой месеци за плащане - цяло число в интервала [1 … 24]
# Изход
# На конзолата се отпечатва 1 ред:
# •	Цената, която заплаща клиентът, форматирана до втория знак след десетичната запетая, в следния формат:
# "{цената} lv."

contract_period = input()
contract_type = input()
internet = input()
months = int(input())

payment_per_month = 0

if contract_period == 'one':
    if contract_type == 'Small':
        payment_per_month = 9.98
    elif contract_type == 'Middle':
        payment_per_month = 18.99
    elif contract_type == 'Large':
        payment_per_month = 25.98
    elif contract_type == 'ExtraLarge':
        payment_per_month = 35.99
elif contract_period == 'two':
    if contract_type == 'Small':
        payment_per_month = 8.58
    elif contract_type == 'Middle':
        payment_per_month = 17.09
    elif contract_type == 'Large':
        payment_per_month = 23.59
    elif contract_type == 'ExtraLarge':
        payment_per_month = 31.79

internet_per_month = 0

if internet == 'yes':
    if payment_per_month <= 10:
        internet_per_month = 5.50
    elif 10 < payment_per_month <= 30:
        internet_per_month = 4.35
    else:
        internet_per_month = 3.85

total_price = months * (payment_per_month + internet_per_month)

if contract_period == 'two':
    total_price = total_price * (1 - 0.0375)

print(f'{total_price:.2f} lv.')