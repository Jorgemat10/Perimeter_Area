import math

def area_perimeter_rectangle(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

def area_perimeter_square(side):
    area = side * side
    perimeter = 4 * side
    return area, perimeter

def area_perimeter_circle(radius):
    area = math.pi * (radius ** 2)
    perimeter = 2 * math.pi * radius
    return area, perimeter

def area_perimeter_triangle(base, height, side1, side2, side3):
    area = 0.5 * base * height
    perimeter = side1 + side2 + side3
    return area, perimeter

def calculator():
    print("Welcome to the Area and Perimeter Calculator!")
    while True:
        print("\nChoose a shape:")
        print("1. Rectangle")
        print("2. Square")
        print("3. Circle")
        print("4. Triangle")
        shape = input("Enter the number of your choice: ")

        if shape == '1':
            length = float(input("Enter the length of the rectangle: "))
            width = float(input("Enter the width of the rectangle: "))
            area, perimeter = area_perimeter_rectangle(length, width)
            print(f"Area: {area}")
            print(f"Perimeter: {perimeter}")
        
        elif shape == '2':
            side = float(input("Enter the side length of the square: "))
            area, perimeter = area_perimeter_square(side)
            print(f"Area: {area}")
            print(f"Perimeter: {perimeter}")
        
        elif shape == '3':
            radius = float(input("Enter the radius of the circle: "))
            area, perimeter = area_perimeter_circle(radius)
            print(f"Area: {area}")
            print(f"Circumference: {perimeter}")
        
        elif shape == '4':
            base = float(input("Enter the base length of the triangle: "))
            height = float(input("Enter the height of the triangle: "))
            side1 = float(input("Enter the length of the first side of the triangle: "))
            side2 = float(input("Enter the length of the second side of the triangle: "))
            side3 = float(input("Enter the length of the third side of the triangle: "))
            area, perimeter = area_perimeter_triangle(base, height, side1, side2, side3)
            print(f"Area: {area}")
            print(f"Perimeter: {perimeter}")
        
        else:
            print("Invalid choice. Please try again.")

        continue_calc = input("Do you want to calculate another shape? (yes/no): ").lower()
        if continue_calc not in ['yes', 'y']:
            break

    print("Thank you for using the calculator!")

calculator()
