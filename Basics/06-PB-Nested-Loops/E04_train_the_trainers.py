# Курсът "Train the trainers" е към края си и финалното оценяване наближава. Вашата задача е да помогнете на журито,
# което ще оценява презентациите, като напишете програма, в която да изчислява средната оценка от представянето
# на всяка една презентация от даден студент, а накрая - средния успех от всички тях.
# От конзолата на първият ред се прочита броят на хората в журито n - цяло число.
# След това на отделен ред се прочита името на презентацията – текст.
# За всяка една презентация на нов ред се четат n - на брой оценки - реално число.
# След изчисляване на средната оценка за конкретна презентация, на конзолата се печата:
#  "{името на презентацията} - {средна оценка}."
# След получаване на команда "Finish", на конзолата се печата "Student's final assessment is {среден успех от
# всички презентации}." и програмата приключва.
# Всички оценки трябва да бъдат форматирани до втория знак след десетичната запетая.

jury_members = int(input())

input_line = input()
total_assessment = 0
count_presentations = 0

while input_line != 'Finish':
    name_presentation = input_line
    count_presentations += 1
    assessment_current_presentation = 0

    for _ in range(jury_members):
        grade = float(input())
        assessment_current_presentation += grade

    avg_current_presentation = assessment_current_presentation / jury_members
    total_assessment += avg_current_presentation
    print(f'{name_presentation} - {avg_current_presentation:.2f}.')

    input_line = input()

avg_total = total_assessment / count_presentations
print(f"Student's final assessment is {avg_total:.2f}.")