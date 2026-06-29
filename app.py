# part 1
# step 1 - Age Converter
try:
    age = input("Enter your age: ")
    next_year = int(age) + 1
    print("Next year you will be", next_year)
except ValueError:
    print("Age must be a number")

# step 2 - Safe Division
try:
    a = int(input("First number: "))
    b = int(input("Second number: "))
    print(a / b)
except ZeroDivisionError:
    print("Cannot divide by zero")