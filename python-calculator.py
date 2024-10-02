def calculator():
    print("Calculator Program")
    
    # Input first number
    print("Please enter number:")
    x = float(input())
    
    # Input second number
    print("Enter another number:")
    y = float(input())
    
    # Select operation
    print("Select operation:")
    print("1. Division (X / Y)")
    print("2. Multiplication (X * Y)")
    print("3. Addition (X + Y)")
    print("4. Subtraction (X - Y)")
    operation = input()
    
    # Perform calculation based on selected operation
    if operation == '1':
        if y != 0:
            result = x / y
        else:
            result = "Error: Division by zero"
    elif operation == '2':
        result = x * y
    elif operation == '3':
        result = x + y
    elif operation == '4':
        result = x - y
    else:
        result = "Invalid operation selected"
    
    # Output result
    print("Result:", result)

# Run the calculator
calculator()
