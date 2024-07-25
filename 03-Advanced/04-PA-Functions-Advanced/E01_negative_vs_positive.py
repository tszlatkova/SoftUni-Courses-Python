# You will receive a sequence of numbers (integers) separated by a single space. Separate
# the negative numbers from the positive. Find the total sum of the negatives and
# positives, and print the following:
# •	On the first line, print the sum of the negatives
# •	On the second line, print the sum of the positives
# •	On the third line:
# o	If the absolute negative number is larger than the positive number:
# 	"The negatives are stronger than the positives"
# o	If the positive number is larger than the absolute negative number:
# 	"The positives are stronger than the negatives"

def positive_negative_sum(*args):
    list_int = [int(x) for x in args]
    positive_sum = 0
    negative_sum = 0

    for num in list_int:
        if num > 0:
            positive_sum += num
        elif num < 0:
            negative_sum += num

    result = f'{negative_sum}\n{positive_sum}\n'

    if abs(negative_sum) > positive_sum:
        result += 'The negatives are stronger than the positives'
    else:
        result += 'The positives are stronger than the negatives'

    return result


input_line = input().split()

print(positive_negative_sum(*input_line))
