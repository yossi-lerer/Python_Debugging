# # part 1
# # step 1 - Age Converter
# try:
#     age = input("Enter your age: ")
#     next_year = int(age) + 1
#     print("Next year you will be", next_year)
# except ValueError:
#     print("Age must be a number")

# # step 2 - Safe Division
# try:
#     a = int(input("First number: "))
#     b = int(input("Second number: "))
#     print(a / b)
# except ZeroDivisionError:
#     print("Cannot divide by zero")
# # step 3 - Number From List
# try:
#     numbers = [10, 20, 30]
#     index = int(input("Choose index: "))
#     print(numbers[index])
# except IndexError:
#     print("Index not found")
# # step 4 - Dictionary Lookup
# prices = {
#     "apple": 3,
#     "banana": 5
# }
# try:
#     item = input("Enter item: ")
#     print(prices[item])
# except KeyError:
#     print("Item not found")
# # step 5 - Multiple Error Types
# numbers = [100, 200, 300]

# try:
#     index = int(input("Choose index: "))
#     divider = int(input("Choose divider: "))

#     result = numbers[index] / divider
#     print(result)
# except IndexError:
#     print("The number it is not index in the list")
# except ZeroDivisionError:
#     print("it is not passible to divishion by zero")
# except ValueError:
#     print("it is not a number in the input")
# # step 6 - Finally Message
# try:
#     score = int(input("Enter score: "))
#     print("Your score is", score)
# except ValueError:
#     print("Invalid score")
# finally:
#     print("Check finished")
# step 7 - Syntax Error vs Runtime Error
name = input("Enter your name: ")
if name == "admin"
    print("Welcome admin")
else:
    print("Welcome user")
