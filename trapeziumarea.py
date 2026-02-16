print("Calculating the area of a trapezium")

length1 = float(input("Enter the first number (one of the lengths): "))
length2 = float(input("Enter the second number (one of the lengths): "))
height = float(input("Enter the third number (the height of the trapezium): "))

area = height * (length1 + length2) / 2

print("The area of the trapezium is", area)