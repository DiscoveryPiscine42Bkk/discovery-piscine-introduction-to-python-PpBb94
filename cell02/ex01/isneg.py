#!/usr/bin/env python3

# รับค่าตัวเลขจากผู้ใช้
try:
    num_str = input("Enter a number: ")
    num = int(num_str)  # แปลงสตริงที่รับมาเป็นจำนวนเต็ม

    # ตรวจสอบเงื่อนไขตามโจทย์
    if num > 0:
        print("This number is positive.")
    elif num < 0:
        print("This number is negative.")
    else:  # num == 0
        print("This number is both positive and negative.")

except ValueError:
    print("Invalid input. Please enter a valid integer.")
except EOFError:
    print("\nInput cancelled.")