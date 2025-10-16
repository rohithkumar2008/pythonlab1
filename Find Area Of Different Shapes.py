import math
def calculate_area():
    print("Choose the shape to calculate the area:")
    print("1. Rectangle")
    print("2. Square")
    print("3. Circle")
    print("4. Triangle") 
choice = int(input("Enter your choice (1/2/3/4): ")) 
if choice == 1:
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = length * width
    print(f"The area of the rectangle is {area}") 
elif choice == 2:
    side = float(input("Enter the side length of the square: "))
    area = side * side
    print(f"The area of the square is {area}") 
elif choice == 3:
    radius = float(input("Enter the radius of the circle: "))
    area = math.pi * radius * radius
    print(f"The area of the circle is {area}") 
elif choice == 4:
    base = float(input("Enter the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = 0.5 * base * height
    print(f"The area of the triangle is {area}") 
else:
    print("Invalid choice. Please select a valid option.") 
