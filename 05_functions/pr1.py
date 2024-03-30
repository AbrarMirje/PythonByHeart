# Function Returning Multiple Values
# Problem: Create a function that returns both the area and circumference of a circle given its radius.

import math
def circle(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference

# We are returning two values from functions, for that we need to variables for store them
a, b = circle(5)

print(f"Area: {a:.2f} and Circumference: {b:.2f}")