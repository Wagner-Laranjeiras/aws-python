# 1. Hello World
print('hello world')

#2. Simple Calc
def calculator():
    print('Step one: Choose an operation: ')
    operation = int(input(
                    '1. Addition\n' 
                    '2. Subtraction\n'
                    '3. Multiplication\n'
                    '4. Division\n'
                ))
    print(operation)
    
    number1 = int(input('Step 2: Type the first number\n'))
    number2 = int(input('Step 3: Type the second number\n'))

    if operation == 1:
        print(f'{number1} + {number2} = {number1 + number2}')
    elif operation == 2:
        print(f'{number1} - {number2} = {number1 - number2}')
    elif operation == 3:
        print(f'{number1} * {number2} = {number1 * number2}')
    elif operation == 4:
        print(f'{number1} / {number2} = {number1 / number2}')
    else:
        print('invalid operation')

# calculator()

# 3. Odd or Even
def OddOrEven(number):
    if number % 2 == 0:
        print(f'{number} is even')
    else:
        print(f'{number} is odd')

# OddOrEven(6)

# 4. FizzBuzz
def FizzBuzz():
    i = 1
    while 100 >= i:
        if i % 15 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)
        i = i + 1

# FizzBuzz()

# 5. Password Validator

# 6. Factorial
def CalculateFactorial(number):
    result = 1
    for i in range(1, (number + 1)):
        result *= i
        print(result)

# CalculateFactorial(6)

# 7. Prime Number
# def CheckForPrimeNumber(number):


# CheckForPrimeNumber(6)

def calculator():
    print('Step one: Choose an operation by inputing its number: ')
    operation = int(input(
                    '1. Addition\n' 
                    '2. Subtraction\n'
                    '3. Multiplication\n'
                    '4. Division\n'
                ))    
    number1 = int(input('Step 2: Type the first number\n'))
    number2 = int(input('Step 3: Type the second number\n'))

    if operation == 1:
        print(f'{number1} + {number2} = {number1 + number2}')
    elif operation == 2:
        print(f'{number1} - {number2} = {number1 - number2}')
    elif operation == 3:
        print(f'{number1} * {number2} = {number1 * number2}')
    elif operation == 4:
        print(f'{number1} / {number2} = {number1 / number2}')
    else:
        print('invalid operation')

calculator()