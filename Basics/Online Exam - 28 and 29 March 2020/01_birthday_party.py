# За рожденният ден на дъщеря си Людмила е решила да организира парти, на което да покани всичките ѝ съученици.
# За целта е решила да наеме развлекателна зала за деца, чийто наем ще получите като вход от конзолата.
# Напишете програма, с която да помогнете на Людмила да изчисли какъв бюджет ще ѝ бъде необходим,
# като имате следната информация за допълнителните неща, необходими за тържеството:
# •	Торта  – цената ѝ е 20% от наема на залата
# •	Напитки – цената им е 45% по-малко от тази на тортата
# •	Аниматор – цената му е 1/3 от цената за наема на залата
# Вход
# От конзолата се четe 1 ред:
# •	Наем за залата – реално число в интервала [100.00..10000.00]
# Изход
# Да се отпечата на конзолата какъв бюджет ще бъде необходим за организиране на тържеството.

rent = float(input())

cake = 0.2 * rent
drinks = 0.55 * cake
animator = 1/3 * rent

total = rent + cake + drinks + animator

print(total)