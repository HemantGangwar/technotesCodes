#!/usr/bin/env python3
import math
import random

n1 = int(input("Enter first number(integer): "))
n2 = int(input("Enter second number(integer): "))

print()
print("Sum of both numbers: ", n1+n2)
print("Subraction of both numbers: ", n1-n2)
print("Multiplication of both numbers: ", n1*n2)
print("Division of both numbers yield quotient: ", n1/n2)
print("Integer division of both numbers yield quotient: ", n1//n2)
print("Module division of both numers yield remainder: ", n1%n2)
print()
print("Generating a random number between (0-20) to perform Mathematical operations")
n3 = random.randint(0,20)
print()
print("Number Generated is: ", n3)
print ("Factorial of ", n3, "is", math.factorial(n3))
print ("Square of ", n3, "is", math.pow(n3,2))