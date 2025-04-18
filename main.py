#!/usr/bin/env python3

from utilities import Colors

class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return (
                f"{Colors.RED}"
                    "Cannot divide by zero"
                f"{Colors.END}"
            )

def main():
	calc = Calculator()
    
	print(Colors.YELLOW)
	print("Welcome to the Basic Calculator!")
	print(Colors.END)
	print("--------------------------------")
	# ↑ you could use print("-"*32)
	
	print(Colors.NEGATIVE)
	print("\nOperations:")
	print(Colors.END)
	print("1. Addition")
	print("2. Subtraction")
	print("3. Multiplication")
	print("4. Division")
    
	try:
		choice = input("\nEnter your choice (1-4): ")
		num1 = float(input("Enter first number: "))
		num2 = float(input("Enter second number: "))
		
		match choice:
			case '1':
				result = calc.add(num1, num2)
				print("\n")
				print(f"{num1} + {num2} = {result}")
			case '2':
				result = calc.subtract(num1, num2)
				print("\n")
				print(f"{num1} - {num2} = {result}")
			case '3':
				result = calc.multiply(num1, num2)
				print("\n")
				print(f"{num1} * {num2} = {result}")
			case '4':
				result = calc.divide(num1, num2)
				print(f"{num1} / {num2} = {result}")
			case _:
				print("Invalid choice.")
	except ValueError:
		print("Invalid input. Please enter numbers only.")
	except Exception as e:
		print(f"An error occurred: {e}")
		print("\n")
		print("Goodbye!")

if __name__ == "__main__":
    main()
