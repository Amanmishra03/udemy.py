def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operation = {
    "+":  add,
    "-":  subtract,
    "*":  multiply,
    "/":  divide
}

num1 = int(input("Enter the first number: "))
for operator in operation:
    print(operator)
operation_symbol = input("pick an operation from the line above: ")
num2 = int(input("Enter the second number: "))
calculation_function = operation[operation_symbol]
print(calculation_function)
first_answer = calculation_function(num1, num2)
print(f"{num1} {operation_symbol} {num2} = {first_answer} ")

operation_symbol = input("pick another opertion: ")
num3 = int(input("what's the next number ?: "))
calculation_function = operation[operation_symbol]
second_answer = calculation_function(first_answer,num3)
print(f"{first_answer} {operation_symbol} {num3} = {second_answer} ")





















