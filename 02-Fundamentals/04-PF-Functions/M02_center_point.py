# You will be given the coordinates of two points on a Cartesian coordinate system - X1, Y1, X2, and Y2 on separate
# lines. Write a function that prints the point which is closest to the center of the coordinate system (0, 0) in the
# format: "({X}, {Y})"
# If the points are at the same distance from the center, print only the first one. The resulting coordinates must be
# formatted to the lower integer.

from math import floor


def closest_to_center(x1, y1, x2, y2):
    """
    The function calculate the length of two lines OA and OB, where O(0;0), A(x1,y1) and B(x2,y2), and return the
    coordinates of the smaller one. If they have the same length, then it returns the first coordinates.

    Note: To calculate which one has smaller length is the same as checking which point is closest to (0,0).
    """
    if (x1 ** 2 + y1 ** 2) <= (x2 ** 2 + y2 ** 2):
        return f'({floor(x1)}, {floor(y1)})'
    else:
        return f'({floor(x2)}, {floor(y2)})'


X1, Y1, X2, Y2 = float(input()), float(input()), float(input()), float(input())

print(closest_to_center(X1, Y1, X2, Y2))

help(closest_to_center)