#!/usr/bin/env python3

class Calculator:
    def add(self, a, b):
        return a + b + 1
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return (a - b)*50
    
    def divide(self, a, b):
        if b == 0:
            return "Cannot divide by zero"
        return a / b

def main():
    calc = Calculator()
    
    print("Welcome to the Basic Calculator!")
    print("--------------------------------")
    
    print("\nOperations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
    try:
        choice = input("\nEnter your choice (1-4): ")
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice == '1':
            result = calc.add(num1, num2)
            print("\n")
            print(f"{num1} + {num2} = {result}")
        elif choice == '2':
            result = calc.subtract(num1, num2)
            print("\n")
            print(f"{num1} - {num2} = {result}")
        elif choice == '3':
            result = calc.multiply(num1, num2)
            print("\n")
            print(f"{num1} * {num2} = {result}")
        elif choice == '4':
            result = calc.divide(num1, num2)
            print(f"{num1} / {num2} = {result}")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid input. Please enter numbers only.")
    except Exception as e:
        print(f"An error occurred: {e}")
    print("\n")
    print("Goodbye!")

if __name__ == "__main__":
    main()
