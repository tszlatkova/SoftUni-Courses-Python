# Create a function that calculates and returns the area of a rectangle by given width and height. Print the result on
# the console.

def area(width, height):
    return width * height


rectangle_width = float(input())
rectangle_height = float(input())

print(int(area(rectangle_width, rectangle_height)))