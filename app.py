# part 1
# step 1
try:
    age = input("Enter your age: ")
    next_year = int(age) + 1
    print("Next year you will be", next_year)
except ValueError:
    print("Age must be a number")