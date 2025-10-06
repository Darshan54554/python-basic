try:
    number = int(input("Enter a number: "))
    print(f"My integer is {number}")

    square = number * number
    cube = number ** 3

    print(f"The square of {number} is {square}")
    print(f"The cube of {number} is {cube}")

except ValueError:
    print("Please enter a valid number!")
