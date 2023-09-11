# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

# Main program loop
while True:
    print("Options:")
    print("Enter 'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter 'multiply' for multiplication")
    print("Enter 'divide' for division")
    print("Enter 'quit' to end the program")

    user_choice = input("Enter your choice: ")

    if user_choice == "quit":
        print("Exiting the program. Goodbye!")
        break
    elif user_choice in ("add", "subtract", "multiply", "divide"):
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if user_choice == "add":
            result = add(num1, num2)
            print(f"Result: {num1} + {num2} = {result}")
        elif user_choice == "subtract":
            result = subtract(num1, num2)
            print(f"Result: {num1} - {num2} = {result}")
        elif user_choice == "multiply":
            result = multiply(num1, num2)
            print(f"Result: {num1} * {num2} = {result}")
        elif user_choice == "divide":
            result = divide(num1, num2)
            print(f"Result: {num1} / {num2} = {result}")
    else:
        print("Invalid input. Please enter a valid option.")
