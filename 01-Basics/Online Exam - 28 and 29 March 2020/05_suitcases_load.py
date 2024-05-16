# Напишете програма, която ви помага при товаренето на куфари в багажника на самолет. Всеки самолет има определен
# капацитет на багажника. До получаване на команда "End" ще получавате обем на куфар. Обемът на всеки трети куфар
# трябва да се увеличава с 10%, поради загубата на пространство при начина на подреждане. Ако свободното
# пространството в даден момент е по-малко от обема на куфар товаренето трябва да прекъсне.
# Вход
# Първоначално се чете един ред:
# •	Капацитетът на багажника – реално число в диапазона [100.0…6000.0]
# След това до получаване на команда "End" или до запълване на багажника, се чете по един ред:
# o	Обем на куфар – реално число в диапазона [100.0…6000.0]
# Изход
# На конзолата да се отпечатат следните редове според случая:
# •	При получаване на командата "End" се печата:
# "Congratulations! All suitcases are loaded!"
# •	Ако обемът на куфара е по-голям от оставащото пространство в багажника:
# "No more space!"
# •	Накрая винаги се отпечатва статистика – колко багажа са натоварени:
# "Statistic: {брой натоварени багажи} suitcases loaded."

capacity = float(input())

count_suitcases = 0
no_more_space = False

input_line = input()

while input_line != 'End':
    count_suitcases += 1
    weight_suitcase = float(input_line)

    if count_suitcases % 3 == 0:
        capacity -= weight_suitcase * 1.10
    else:
        capacity -= weight_suitcase

    if capacity < 0:
        no_more_space = True
        count_suitcases -= 1
        break

    input_line = input()

if no_more_space:
    print(f'No more space!')
else:
    print(f'Congratulations! All suitcases are loaded!')

print(f'Statistic: {count_suitcases} suitcases loaded.')