"""
Write a program that takes an integer input and checks if it's even number.
Prints out 'True' if the number is even and 'False' if the number is not even.

e.g.
Input: 2
Output: 2 is even

Input: 3
Output: 3 is not even
"""

user_number = int(input("Please input a number to determine if its even: "))

if user_number % 2 == 0:
    print("True")
else:
    print("False")