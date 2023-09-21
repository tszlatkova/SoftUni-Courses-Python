# Ани обича да пътува и иска тази година да посети няколко различни дестинации. Като си избере дестинация,
# ще прецени колко пари ще й трябват, за да отиде до там, и ще започне да спестява. Когато е спестила достатъчно,
# ще може да пътува.
# От конзолата всеки път ще се четат първо дестинацията и минималния бюджет (десетично число), който ще е нужен за
# пътуването.
# След това ще се четат няколко суми (десетични числа), които Ани спестява като работи и когато успее да събере
# достатъчно за пътуването, ще заминава, като на конзолата трябва да се изпише: "Going to {дестинацията}!"
# Когато е посетила всички дестинации, които иска, вместо дестинация ще въведе "End" и програмата ще приключи.

input_line = input()

while input_line != 'End':
    destination = input_line
    needed_money = float(input())

    total_saved = 0
    while total_saved < needed_money:
        saved = float(input())
        total_saved += saved

    print(f'Going to {destination}!')
    input_line = input()