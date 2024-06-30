from telnetlib import theNULL


first_number = input("Enter the first number:")
first_number = int(first_number)
print(f'number:{first_number}')

second_number = input("Enter the second number:")
second_number = int(second_number)
print(f'number:{second_number}')

operation = input("Choose an operation (+, -, *, /):")
print(f'operation: {operation}')

if operation == '+':
    result = first_number + second_number
    print(f"result:{result}")
elif operation == '-':
    result = first_number - second_number
    print(f"result:{result}")
elif operation == '*':
    result = first_number * second_number
    print(f"result:{result}")
elif operation == '/':
    result = first_number / second_number
    print(f"result:{result}")