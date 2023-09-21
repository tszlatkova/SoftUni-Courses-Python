# Частно училище организира лагери за учениците по време на ваканциите. В зависимост от вида на ваканцията (пролетна,
# лятна или зимна) и вида на групата (момчета/момичета или смесена) цената на нощувката в хотела е различна,
# както и спортът, който ще практикуват учениците.

# 	                    Зимна ваканция	            Пролетна ваканция               	Лятна ваканция
# момчета/момичета	        9.60	                    7.20	                            15
# смесена група	            10	                        9.50	                            20

# Училището получава отстъпка от крайната цена, в зависимост от броя на настанените в хотела ученици:
# •	Ако броят на учениците е 50 или повече, училището получава 50% отстъпка
# •	Ако броят на учениците е 20 или повече и в същото време по-малък от 50, училището получава 15% отстъпка
# •	Ако броят на учениците е 10 или повече и в същото време по-малък от 20, училището получава 5% отстъпка

# В таблицата по-долу са дадени спортовете, които ще се практикуват в зависимост от вида на ваканцията и групата:
# 	                    Зимна ваканция	            Пролетна ваканция	              Лятна ваканция
# момичета	                Gymnastics	                Athletics	                    Volleyball
# момчета	                Judo	                    Tennis	                         Football
# смесена група	            Ski	                        Cycling	                         Swimming
# Да се напише програма, която пресмята цената, която ще заплати училището за нощувките и принтира спорта, който ще се
# практикува от учениците.
# Вход
# От конзолата се четат 4 реда:
# 1.	Сезонът – текст - “Winter”, “Spring” или “Summer”;
# 2.	Видът на групата – текст - “boys”, “girls” или “mixed”;
# 3.	Брой на учениците – цяло число в интервала [1 … 10000];
# 4.	Брой на нощувките – цяло число в интервала [1 … 100].
# Изход
# На конзолата се отпечатва 1 ред:
# •	Спортът, който са практикували учениците и цената за нощувките, която е заплатило училището, форматирана до
# втория знак след десетичната запетая, в следния формат:
# "{спортът} {цената} lv.“

season = input()
group = input()
students = int(input())
nights = int(input())

price_per_student = 0

if group == 'boys' or group == 'girls':
    if season == 'Winter':
        price_per_student = 9.60
    elif season == 'Spring':
        price_per_student = 7.20
    elif season == 'Summer':
        price_per_student = 15
elif group == 'mixed':
    if season == 'Winter':
        price_per_student = 10
    elif season == 'Spring':
        price_per_student = 9.50
    elif season == 'Summer':
        price_per_student = 20

total = price_per_student * students * nights

if 10 <= students < 20:
    total = total * 0.95
elif 20 <= students < 50:
    total = total * 0.85
elif students >= 50:
    total = total * 0.50

sport = ''

if group == 'girls':
    if season == 'Winter':
        sport = 'Gymnastics'
    elif season == 'Spring':
        sport = 'Athletics'
    elif season == 'Summer':
        sport = 'Volleyball'
elif group == 'boys':
    if season == 'Winter':
        sport = 'Judo'
    elif season == 'Spring':
        sport = 'Tennis'
    elif season == 'Summer':
        sport = 'Football'
elif group == 'mixed':
    if season == 'Winter':
        sport = 'Ski'
    elif season == 'Spring':
        sport = 'Cycling'
    elif season == 'Summer':
        sport = 'Swimming'

print(f'{sport} {total:.2f} lv.')