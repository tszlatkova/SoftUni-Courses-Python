# Джеси е решила да събира пари за екскурзия и иска от вас да ѝ помогнете да разбере дали ще
# успее да събере необходимата сума. Тя спестява или харчи част от парите си всеки ден.
# Ако иска да похарчи повече от наличните си пари, то тя ще похарчи колкото има и ще ѝ останат 0 лева.
# Вход
# От конзолата се четат:
# •	Пари, нужни за екскурзията - реално число;
# •	Налични пари - реално число.
# След това многократно се четат по два реда:
# •	Вид действие – текст с две възможности: "spend" или "save";
# •	Сумата, която ще спести/похарчи - реално число.
# Изход
# Програмата трябва да приключи при следните случаи:
# •	Ако 5 последователни дни Джеси само харчи, на конзолата да се изпише:
# o	"You can't save the money."
# o	"{Общ брой изминали дни}"
# •	Ако Джеси събере парите за почивката, на конзолата се изписва:
# o	"You saved the money for {общ брой изминали дни} days."

needed_money = float(input())
money_now = float(input())

saved_money = money_now
count_days = 0
count_spend_days = 0

while saved_money < needed_money:
    spend_or_save = input()
    money = float(input())
    count_days += 1

    if spend_or_save == 'save':
        saved_money += money
        count_spend_days = 0
    elif spend_or_save == 'spend':
        count_spend_days += 1
        saved_money -= money

        if count_spend_days == 5:
            print(f"You can't save the money.")
            print(f'{count_days}')
            break

        if saved_money < 0:
            saved_money = 0
else:
    print(f'You saved the money for {count_days} days.')