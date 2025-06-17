#!/usr/bin/env python3

# Prompt the user to enter a number
try:
    num_str = input("Enter a number: ")
    num = int(num_str)  # Convert the input string to an integer

    # Check if the number is equal to zero
    if num == 0:
        print("This number is equal to zero.")
    else:
        print("This number is different from zero.")

except ValueError:
    print("Invalid input. Please enter a valid integer.")
except EOFError:
    print("\nInput cancelled.")
