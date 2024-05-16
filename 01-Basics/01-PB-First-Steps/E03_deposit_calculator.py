# Напишете програма, която изчислява каква сума ще получите в края на депозитния период при определен лихвен
# процент. Използвайте следната формула:
# сума = депозирана сума  + срок на депозита * ((депозирана сума * годишен лихвен процент ) / 12)

# Вход
# От конзолата се четат 3 реда:
# 1.	Депозирана сума – реално число в интервала [100.00 … 10000.00]
# 2.	Срок на депозита (в месеци) – цяло число в интервала [1…12]
# 3.	Годишен лихвен процент – реално число в интервала [0.00 …100.00]

deposit = float(input())
if 100 <= deposit <= 10000:
    months = int(input())
    if 1 <= months <= 12:
        percentage = float(input())
        if 0 <= percentage <= 100:
            total = deposit + months*deposit*percentage/1200
            print(total)
        else:
            print("Not valid percentage!")
    else:
        print("Not valid number of months!")
else:
    print("Not valid sum for deposit!")
