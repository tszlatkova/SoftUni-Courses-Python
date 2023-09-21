# Напишете програма, която при въведени градуси (реално число) принтира какво е времето,
# като имате предвид следната таблица:

# Градуси	Време
# 26.00 - 35.00	Hot
# 20.1 - 25.9	Warm
# 15.00 - 20.00	Mild
# 12.00 - 14.9	Cool
# 5.00 - 11.9	Cold

# Ако се въведат градуси, различни от посочените в таблицата, да се отпечата "unknown".

degrees = float(input())

if 26.00 <= degrees <= 35:
    print('Hot')
elif 20.10 <= degrees <= 25.90:
    print('Warm')
elif 15.00 <= degrees <= 20.00:
    print('Mild')
elif 12.00 <= degrees <= 14.90:
    print('Cool')
elif 5.00 <= degrees <= 11.90:
    print('Cold')
else:
    print('unknown')
