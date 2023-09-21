# Напишете програма която, чете ден от седмицата (текст), на английски език - въведен от потребителя.
# Ако денят е работен отпечатва на конзолата - "Working day", ако е почивен - "Weekend". Ако се въведе текст
# различен от ден от седмицата да се отпечата - "Error".

day = input()

if day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:
    print('Working day')
elif day in ['Saturday', 'Sunday']:
    print('Weekend')
else:
    print('Error')


