def addition(num1: int, num2:int):
    return num1 + num2

def subtraction(num1:int, num2:int):
    return num1 - num2

def multiplication(num1:int, num2:int):
    return num1 * num2

def division(num1:int, num2:int):
    if num2 !=0:
        return num1 / num2
    else:
        return "Cannot divide with zero!"

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print(f'Sum: {addition(num1, num2)}')
print(f'Difference : {subtraction(num1, num2)}')
print(f'Product = {multiplication(num1, num2)}')
print(f'Quotient = {division(num1, num2)}')