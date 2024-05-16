# Магазин за цветя предлага 3 вида цветя: хризантеми, рози и лалета. Цените зависят от сезона.
# Сезон         	Хризантеми	        Рози	            Лалета
# Пролет / Лято	    2.00 лв./бр.	    4.10 лв./бр.	    2.50 лв./бр.
# Есен / Зима	    3.75 лв./бр.	    4.50 лв./бр.	    4.15 лв./бр.
# В празнични дни цените на всички цветя се увеличават с 15%. Предлагат се следните отстъпки:
# •	За закупени повече от 7 лалета през пролетта – 5% от цената на целият букет.
# •	За закупени 10 или повече рози през зимата – 10% от цената на целият букет.
# •	За закупени повече от 20 цветя общо през всички сезони – 20% от цената на целият букет.
# Отстъпките се правят по така написания ред и могат да се наслагват! Всички отстъпки важат след
# оскъпяването за празничен ден!
# Цената за аранжиране на букета винаги е 2лв. Напишете програма, която изчислява цената за един букет.
# Вход
# Входът се чете от конзолата и съдържа точно 5 реда:
# •	На първия ред е броят на закупените хризантеми – цяло число в интервала [0 ... 200]
# •	На втория ред е броят на закупените рози – цяло число в интервала [0 ... 200]
# •	На третия ред е броят на закупените лалета – цяло число в интервала [0 ... 200]
# •	На четвъртия ред е посочен сезона – [Spring, Summer, Аutumn, Winter]
# •	На петия ред е посочено дали денят е празник – [Y – да / N - не]
# Изход
# Да се отпечата на конзолата 1 число – цената на цветята, форматирана до вторият знак след десетичната запетая.

chrysanthemum = int(input())
rose = int(input())
tulip = int(input())
season = input()
weekday_or_not = input()

chrysanthemum_price = 0
rose_price = 0
tulip_price = 0
total = 0

if season == 'Spring' or season == 'Summer':
    if weekday_or_not == 'Y':
        chrysanthemum_price = chrysanthemum * 2 * 1.15
        rose_price = rose * 4.10 * 1.15
        tulip_price = tulip * 2.50 * 1.15
    elif weekday_or_not == 'N':
        chrysanthemum_price = chrysanthemum * 2
        rose_price = rose * 4.10
        tulip_price = tulip * 2.50
elif season == 'Autumn' or season == 'Winter':
    if weekday_or_not == 'Y':
        chrysanthemum_price = chrysanthemum * 3.75 * 1.15
        rose_price = rose * 4.50 * 1.15
        tulip_price = tulip * 4.15 * 1.15
    elif weekday_or_not == 'N':
        chrysanthemum_price = chrysanthemum * 3.75
        rose_price = rose * 4.50
        tulip_price = tulip * 4.15

total = chrysanthemum_price + rose_price + tulip_price

if season == 'Spring' and tulip > 7:
    total = total * 0.95
elif season == 'Winter' and rose >= 10:
    total = total * 0.90

if (chrysanthemum + rose + tulip) > 20:
    total = total * 0.80

total = total + 2

print(f'{total:.2f}')