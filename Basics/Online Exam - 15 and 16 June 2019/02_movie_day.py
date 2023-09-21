# Вие сте режисьор на филма "Програмирането е забавно", като имате определено време за снимки. От вас се иска да
# напишете програма, с която ще разберете дали снимачният ден ще ви стигне да заснемете филма. Снимачният ден започва
# с подготовка на терен, което е 15 процента от времето за снимки! Филмът има определен брой сцени, които се заснемат
# за определено време.

# Вход
# От конзолата се четат 3 реда:
# 1.	Време за снимки – цяло число в диапазона [0… 1440]
# 2.	Брой сцени  – цяло число в диапазона [5… 25]
# 3.	Времетраене на сцена – цяло число в диапазона [20… 90]

# Изход
# На конзолата да се отпечата един ред:
# •	Ако времето за заснемане на филма ви стигне:
#   "You managed to finish the movie on time! You have {останало време} minutes left!"
# •	Ако времето НЕ ВИ стигне:
#   "Time is up! To complete the movie you need {нужно време} minutes."
# Останалото време да се закръгли до най-близкото цяло число.

scenes_time = int(input())
scenes_number = int(input())
time_per_scene = int(input())

total_time = 0.15 * scenes_time + scenes_number * time_per_scene
diff = abs(total_time - scenes_time)

if total_time <= scenes_time:
    print(f'You managed to finish the movie on time! You have {round(diff)} minutes left!')
else:
    print(f'Time is up! To complete the movie you need {round(diff)} minutes.')