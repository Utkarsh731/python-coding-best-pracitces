# Good practice
try:
    result = int(input("Enter a number: "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
