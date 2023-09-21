# Предстои Вело състезание за благотворителност в което участниците са разпределени в младша("juniors")
# и старша("seniors") група. Парите се набавят от таксата за участие на велосипедистите. Според възрастовата група и
# вида на трасето на което ще се провежда състезанието, таксата е различна.

# Група     	trail   	cross-country   	downhill    	road
# juniors   	5.50	        8	             12.25	         20
# seniors	    7	            9.50	         13.75	         21.50

# Ако в "cross-country" състезанието се съберат 50 или повече участника(общо младши и старши), таксата  намалява с 25%.
# Организаторите отделят 5% процента от събраната сума за разходи.

# Вход
# От конзолата се четат 2 числа и един стринг, всяко на отделен ред:
# •	Първият ред – броят младши велосипедисти. Цяло число в интервала [1…100]
# •	Вторият ред – броят старши велосипедисти. Цяло число в интервала [1… 100]
# •	Третият ред – вид трасе – "trail", "cross-country", "downhill" или "road"

# Изход
# Да се отпечата на конзолата едно число:
# "{дарената сума}" - форматирана с точност до 2 знака след десетичната запетая.

juniors = int(input())
seniors = int(input())
road_type = input()

total = 0
expense = 0
donation = 0

if road_type == 'trail':
    total = juniors * 5.50 + seniors * 7
elif road_type == 'cross-country':
    if juniors + seniors >= 50:
        total = (juniors * 8 + seniors * 9.50) * 0.75
    else:
        total = juniors * 8 + seniors * 9.50
elif road_type == 'downhill':
    total = juniors * 12.25 + seniors * 13.75
elif road_type == 'road':
    total = juniors * 20 + seniors * 21.50

expense = total * 0.05
donation = total - expense

print(f'{donation:.2f}')

