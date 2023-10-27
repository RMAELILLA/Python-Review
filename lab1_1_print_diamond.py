print("This program display '*' as an argument from your input")
# Write python function named "print_diamond" that takes an odd integer n as an argument
def print_diamond(user_n):
    if user_n % 2 == 0:
        print("Please provide an odd integer")
        return
    
    # For n = user_n
    # prints a diamond shape with a width of n using the "*" character.
    for i in range(user_n//2 + 1):
        spaces = ' ' * (user_n//2 - i)
        diamond = '*' * (2 * i + 1)
        print(spaces + diamond)

    for i in range (user_n//2 - 1, -1, -1):
        spaces = ' ' * (user_n//2 - i)
        diamond = '*' * (2 * i + 1)
        print(spaces + diamond)

while True:
    user_d = (input("Do you want to continue? y/n: "))
    user_d = user_d.lower()

    if user_d == "y":
        try:
            user_n = int(input("Please provide a number: "))
            print_diamond(user_n)
        except ValueError:
            print("Field cannot include non-integer or non-numerical values or be blank.")
            continue

    elif user_d == "n":
        print("Thank you for running this program. Have a Good day!")
        break
    else:
        print("Please choose 'y' only if yes or 'n' only if no")
        continue