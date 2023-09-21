# С наближаването на световното първенство по снукър в театъра Крусибъл в Шефилд, Англия, феновете нямат търпение
# да се сдобият с ценните билети. Заради големия наплив от хора, организаторите ви молят да напишете програма за
# продаване на билети, като се има предвид следния ценоразпис:
# 	Четвъртфинал	Полуфинал	Финал
# Стандартен	55.50 £/бр.	75.88 £/бр.	110.10 £/бр.
# Премиум	105.20 £/бр.	125.22 £/бр.	160.66 £/бр.
# ВИП	118.90 £/бр.	300.40 £/бр.	400 £/бр.
# При закупуване на билет, зрителят може да избере опция, снимка с трофея, на цена 40 лири.
# При достигане на определена сума има отстъпки:
# •	Над 4000 лири има 25% отстъпка и безплатни снимки с трофея (ако  опцията за снимки е избрана, таксата от 40 лири
# за билет не се включва)
# •	Над 2500 лири има 10% отстъпка
# При избрана опция за снимки с трофея, цената се начислява след изчисляването на отстъпките.
# Вход
# От конзолата се четат 3 реда:
# 1.	Етап на първенството – текст - “Quarter final ”, “Semi final” или “Final”
# 2.	Вид на билета – текст - “Standard”, “Premium” или “VIP”
# 3.	Брой билети – цяло число в интервала [1 … 30]
# 4.	Снимка с трофея – символ – 'Y' (да) или 'N' (не)
# Изход
# На конзолата се отпечатва 1 ред:
# •	"Цената, която трябва да се заплати, форматирана до втората цифра след десетичния знак"

stage = input()
ticket_type = input()
tickets_number = int(input())
photo = input()

price_per_ticket = 0
total_price = 0

if stage == 'Quarter final':
    if ticket_type == 'Standard':
        price_per_ticket = 55.50
    elif ticket_type == 'Premium':
        price_per_ticket = 105.20
    elif ticket_type == 'VIP':
        price_per_ticket = 118.90
elif stage == 'Semi final':
    if ticket_type == 'Standard':
        price_per_ticket = 75.88
    elif ticket_type == 'Premium':
        price_per_ticket = 125.22
    elif ticket_type == 'VIP':
        price_per_ticket = 300.40
elif stage == 'Final':
    if ticket_type == 'Standard':
        price_per_ticket = 110.10
    elif ticket_type == 'Premium':
        price_per_ticket = 160.66
    elif ticket_type == 'VIP':
        price_per_ticket = 400

total_price_without_discount = price_per_ticket * tickets_number

if total_price_without_discount > 4000:
    total_price = total_price_without_discount * 0.75
elif total_price_without_discount > 2500:
    total_price = total_price_without_discount * 0.90
else:
    total_price = total_price_without_discount

if photo == 'Y' and total_price_without_discount <= 4000:
    total_price += tickets_number * 40

print(f'{total_price:.2f}')