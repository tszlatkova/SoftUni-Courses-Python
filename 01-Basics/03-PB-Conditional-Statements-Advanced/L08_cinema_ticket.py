# Да се напише програма която чете ден от седмицата (текст) – въведен от потребителя и принтира на
# конзолата цената на билет за кино според деня от седмицата:
#
# Monday	Tuesday	Wednesday	Thursday	Friday	Saturday	Sunday
# 12	      12	    14	       14	      12	   16	      16

day = input()

price = 0

if day == 'Monday':
    price = 12
elif day == 'Tuesday':
    price = 12
elif day == 'Wednesday':
    price = 14
elif day == 'Thursday':
    price = 14
elif day == 'Friday':
    price = 12
elif day == 'Saturday':
    price = 16
elif day == 'Sunday':
    price = 16

print(price)