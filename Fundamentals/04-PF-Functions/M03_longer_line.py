# You will be given the coordinates of four points. The first and the second pair of points form two different lines.
# Create a function that prints the longer line in the format "({X1}, {Y1})({X2}, {Y2})" starting from the point which
# is closer to the center of the coordinate system (0, 0). You can reuse the method that you wrote for the previous
# problem. If the lines are of equal length, print only the first one. The resulting coordinates must be formatted
# to the lower integer.

from math import floor


def closest_to_center(x1, y1, x2, y2):
    if (x1 ** 2 + y1 ** 2) <= (x2 ** 2 + y2 ** 2):
        return f'({floor(x1)}, {floor(y1)})({floor(x2)}, {floor(y2)})'
    else:
        return f'({floor(x2)}, {floor(y2)})({floor(x1)}, {floor(y1)})'


def longer_line(x1, y1, x2, y2, x3, y3, x4, y4):

    if ((x1 - x2) ** 2 + (y1 - y2) ** 2) >= ((x3 - x4) ** 2 + (y3 - y4) ** 2):
        return closest_to_center(x1, y1, x2, y2)
    else:
        return closest_to_center(x3, y3, x4, y4)


X1, Y1, X2, Y2 = float(input()), float(input()), float(input()), float(input())
X3, Y3, X4, Y4 = float(input()), float(input()), float(input()), float(input())

print(longer_line(X1, Y1, X2, Y2, X3, Y3, X4, Y4))