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
# step 3 - Number From List
try:
    numbers = [10, 20, 30]
    index = int(input("Choose index: "))
    print(numbers[index])
except IndexError:
    print("Index not found")
# step 4 - Dictionary Lookup
prices = {
    "apple": 3,
    "banana": 5
}
try:
    item = input("Enter item: ")
    print(prices[item])
except KeyError:
    print("Item not found")
# step 5 - Multiple Error Types
numbers = [100, 200, 300]

try:
    index = int(input("Choose index: "))
    divider = int(input("Choose divider: "))

    result = numbers[index] / divider
    print(result)
except IndexError:
    print("The number it is not index in the list")
except ZeroDivisionError:
    print("it is not passible to divishion by zero")
except ValueError:
    print("it is not a number in the input")
# step 6 - Finally Message
try:
    score = int(input("Enter score: "))
    print("Your score is", score)
except ValueError:
    print("Invalid score")
finally:
    print("Check finished")
# step 7 - Syntax Error vs Runtime Error
name = input("Enter your name: ")
if name == "admin":
    print("Welcome admin")
else:
    print("Welcome user")
# The problem here is a syntax error. try except is a solution for observable or unobservable logic errors that are not directly related to code syntax.
# step 8 - Wrong Discount
price = 100
discount = 20

final_price = (price / 100) * (100 - discount)
print(final_price)
# 99.8
# The problem you had was a mistake in writing the calculation process.
# This created a situation where the calculation was the price minus the discount divided by 100, which is not a percentage calculation process.
# step 9 - Login Attempts Logic Bug
password = "abc123"
guess = input("Enter password: ")

if guess == password:
    print("Login successful")
else:
    print("Wrong password")
# The bug is a logical bug. The mistake is that the system logs in users who type an incorrect password.
# the bug is in the line 77
# step 10 - Safe Calculator
try:
    num1 = int(input("Number 1: "))
    op = input("Operator: ")
    num2 = int(input("Number 2: "))
    if op == "+":
        print(num1 + num2)
    elif op == "-":
        print(num1 - num2)
    elif op == "*":
        print(num1 * num2)
    elif op == "/":
        print(num1 / num2)
    else:
        print("Unknown operator")
except ValueError:
    print("plese dont enter not a number")
except ZeroDivisionError:
    print("zero division")
finally:
    print("Calculator closed")
# part 2
# step 1 - Temperature Converter
try:
    celsius = input("Celsius: ")
    # the next line is risky line
    fahrenheit = int(celsius) * 9 / 5 + 32 
    print(fahrenheit)
except ValueError:
    print("Temperature must be a number")
# step 2 - First Letter
try:
    word = input("Enter word: ")
    print(word[0])
except IndexError:
    print("Word is empty")
# step 3 - Average Score
scores = [90, 80, 100]
total = 0
for score in scores:
    total += score
print(total)

average = total / len(scores)
print(average)
# output is 33.333333333333336
# logic bug
# step 4 - Product Price
products = {
    "pen": 4,
    "notebook": 12
}
try:
    product = input("Product: ")
    amount = int(input("Amount: "))

    print(products[product] * amount)
except ValueError:
    print("the amout must be a number")
except KeyError:
    print("the product must contain ")
# step 5 - File Name Check Without File Handling
files = ["data.txt", "users.csv", "notes.txt"]

try:
    choice = int(input("Choose file number: "))
    print(files[choice])
except ValueError:
    print("must be a number")
except IndexError:
    print("no file in this index")
# step 6 - Wrong Maximum
numbers = [4, 10, 2, 8]
maximum = 0

for number in numbers:
    if number > maximum:
        maximum = number

print(maximum)
# wrong output is 0 
# the bug is logic bug in loop
# step 7 - User Profile 
user = {
    "name": "Dana",
    "age": 25
}
try:
    field = input("Choose field: ")
    print(user[field].upper())
except AttributeError:
    print("it is not passible to uppercase a number")
except KeyError:
    print("the key not find")
# step 8 - Order Total 
try:
    price = int(input("Price: "))
    amount = int(input("Amount: "))

    print(f"the price before discount {price}")
    if amount > 3:
        total = (price / 100) * 100 - amount
    print(f"the price before discount {total}")
except ValueError:
    print("all must be a number")
# step 9 - Grade System
try:
    grade = int(input("Grade: "))

    if grade >= 90:
        print("Excellent")
    elif grade >= 70:
        print("Good")
    elif grade >= 55:
        print("Pass")
    else:
        print("Fail")
    # the bug is logic bug
    # The error in the test is that it continues to check the cells even though it found one condition.
except ValueError:
    print("the score must be a number")
# step 10 - Mini Bank Action
balance = 100

try:
    action = input("Action: ")
    amount = int(input("Amount: "))

    if action == "deposit":
        print(f"balance is {balance}")
        balance = balance + amount
        print(f"new balance is {balance}")
    elif action == "withdraw":
        if amount > balance:
            print("Not enough money")
        else: 
            print(f"balance is {balance}")
            balance = balance - amount
            print(f"new balance is {balance}")

    else:
        print("Unknown action")
    print("Balance:", balance)
except ValueError:
    print("amout must be a number")
finally:
    print("Bank action finished")