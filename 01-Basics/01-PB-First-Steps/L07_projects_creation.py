# Напишете програма, която изчислява колко часа ще са необходими на един архитект, за да изготви
# проектите на няколко строителни обекта. Изготвянето на един проект отнема три часа.

# Вход
# От конзолата се четат 2 реда:
# 1.	Името на архитекта - текст
# 2.	Брой на проектите, които трябва да изготви - цяло число в интервала [0 … 100]

# Изход
# На конзолата се отпечатва:
# •	"The architect {името на архитекта} will need {необходими часове} hours to complete
# {брой на проектите} project/s

name = str(input())

numbers_projects = int(input())

hours_projects = 3*numbers_projects

print(f'The architect {name} will need {hours_projects} hours to complete {numbers_projects} project/s.')