#!/usr/bin/env python3

print("""Welcome to Python
        This is a multi line output
                        Displaying print under triple quotes.""")

print("Enter Your name")

customName = input()

customAge = int(input("Enter your Age (in numbers): "))

n1 = int(input("Enter a random integer number: "))
n2 = int(input("Enter another random integer number: "))

print("Hello", customName, "Your Age is: ", customAge, " & Multiplication of both the numbers is: ", n1*n2 )

print()
print("Printing a list seperated by tab")
l1=[1,2,3,4,5]
print(*l1,sep='-->')