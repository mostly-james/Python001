#Function/Method - A block of code used to perform a task

#Inbuilt Functions - Already Exists
print("Inbuilt Functions")
y = max(100, 200, 300, 50, 30, 10, 0)
print("The maximum value is: ", y)

p = min(100, 200, 300, 50, 30, 10, 0)
print("The minimum value is: ", p)

print()

#User-Defined Functions - Created by user
print("User-Defined Functions")
def presidentruto():
    print("Huyu jamaa ni wantam")
presidentruto()

print()

print("Adding using User Defined Functions")
#Parameters/Variables(the placeholders e.g. number1, number2)
#Arguments/Values(the numbers themselves e.g. 3,4,5)
def together(number1, number2):
    print("The sum of the numbers is:", number1 + number2)
together(2, 5)
together(3, 4)
together(4, 6)

