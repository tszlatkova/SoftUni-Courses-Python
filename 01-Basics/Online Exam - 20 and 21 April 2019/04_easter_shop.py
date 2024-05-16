# Покрай великденските празници, квартален магазин започва да продава боядисани яйца. Вашата задача е да напишете
# програма, която да изчислява колко яйца са продадени, като знаете началната им бройка в магазина. По време на
# продажбата е възможно да бъдат доставени допълнителни бройки яйца. Ако в даден момент от изпълнението на програмата,
# клиент поиска да купи повече, отколкото има в наличност, или се получи команда "Close", програмата трябва да приключи
# изпълнение.
# Вход
# От конзолата се чете:
# •	На първи ред - Началното количество яйца в магазина - цяло число в интервала [1… 10000]
# •	След това поредица от два реда (до получаване на команда "Close" или при заявка за купуване на повече от наличните
# в магазина яйца) :
# o	Команда за купуване или допълване на яйца в магазина – текст ("Buy" или "Fill")
# o	Брой на яйца, които да бъдат купени или допълнени в магазина – цяло число в интервала
# [1… 1000]
# Изход
# На конзолата да се отпечатат два реда според случая:
# •	При получаване на командата "Close":
# o	"Store is closed!"
# o	"{броя на продадените общо яйца} eggs sold."
# •	При заявка за покупка на повече яйца, отколкото има в магазина:
# o	"Not enough eggs in store!"
# o	"You can buy only {броя на останалите в магазина яйца}."

starting_quantity_eggs = int(input())

not_enough_eggs = False
input_line = input()
total_sold_eggs = 0

while input_line != 'Close':
    action = input_line
    action_quantity = int(input())

    if action == 'Fill':
        starting_quantity_eggs += action_quantity
    elif action == 'Buy':
        if action_quantity > starting_quantity_eggs:
            not_enough_eggs = True
            break
        else:
            total_sold_eggs += action_quantity
            starting_quantity_eggs -= action_quantity

    input_line = input()

if not_enough_eggs:
    print(f'Not enough eggs in store!')
    print(f'You can buy only {starting_quantity_eggs}.')
else:
    print(f'Store is closed!')
    print(f'{total_sold_eggs} eggs sold.')