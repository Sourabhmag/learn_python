import math


def circle_calc(rad):
    area_cir = math.pi * (rad ** 2)
    circumference_cir = 2 * math.pi * rad
    diameter_cir = 2 * rad
    return area_cir, circumference_cir, diameter_cir


if __name__ == "__main__":
    radius = float(input("Enter radius of Circle\n"))
    area, circumference, diameter = circle_calc(radius)
    print("Area = ", round(area, 2), "\nCircumference = ", round(circumference, 2), "\ndiameter = ", round(diameter, 2))
