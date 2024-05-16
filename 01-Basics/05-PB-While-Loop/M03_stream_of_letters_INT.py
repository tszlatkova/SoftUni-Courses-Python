# Напишете програма, която прочита скрито съобщение в поредица от символи. Те се получават по един на ред до получаване
# на командата "End". Думите се образуват от буквите в реда на четенето им. Символите, които не са латински букви
# трябва да бъдат игнорирани. Думите скрити в потока са разделени от тайна команда от три букви – "c", "o" и "n".
# При първото получаване на една от тези букви, тя се маркира като срещната, но не се запазва в думата. При всяко
# следващо нейно срещане се записва нормално в думата. След като са налични и трите символа от командата, се печата
# думата и интервал " ". Започва се нова дума, която по същия начин чака тайната команда, за да бъде отпечатана.
# Вход
# От конзолата се чете поредица от редове с един символ на всеки до получаване на командата "End".
# Изход
# На конзолата се печата на един ред всяка дума след тайната команда, следвана от интервал.

# for i in range(ord('a'), ord('z')+1):
#     print(chr(i))

# txt = "CompanyX"
#
# x = txt.isalpha()
#
# print(x)

input_line = input()
word, con, output_line = '', '', ''
c_count, o_count, n_count = 0, 0, 0

while input_line != 'End':

    if input_line.isalpha():
        to_add = input_line

        if to_add == 'c':
            c_count += 1

            if c_count == 1:
                con = con + to_add
                input_line = input()

                if con in ['con', 'ocn', 'onc', 'cno', 'nco', 'noc']:
                    to_add = ' '
                    c_count, o_count, n_count, con = 0, 0, 0, ''
                    output_line = output_line + word + to_add
                    word = ''
                    continue
            else:
                word = word + to_add
                input_line = input()
                continue

        elif to_add == 'o':
            o_count += 1

            if o_count == 1:
                con = con + to_add
                input_line = input()

                if con in ['con', 'ocn', 'onc', 'cno', 'nco', 'noc']:
                    to_add = ' '
                    c_count, o_count, n_count, con = 0, 0, 0, ''
                    output_line = output_line + word + to_add
                    word = ''
                    continue
            else:
                word = word + to_add
                input_line = input()
                continue

        elif to_add == 'n':
            n_count += 1

            if n_count == 1:
                con = con + to_add
                input_line = input()

                if con in ['con', 'ocn', 'onc', 'cno', 'nco', 'noc']:
                    to_add = ' '
                    c_count, o_count, n_count, con = 0, 0, 0, ''
                    output_line = output_line + word + to_add
                    word = ''
                    continue
            else:
                word = word + to_add
                input_line = input()
                continue

        else:
            word = word + to_add
            input_line = input()

    else:
        input_line = input()

print(output_line)