# Printing number from a range 5-9
print(list(range(5,10)))

# Printing number from default value 0 i.e., 0-14
print(list(range(15)))

# Printing range with step function
print(list(range(2, 19, 4)))

# Negative step or reverse a number
print(list(range(10, 0, -1)))

# A general for loop printing first 10 numbers
for number in range(11):
    print(number)

# A general for loop printing first 10 numbers and their squares
for number in range(11):
    print(number, '   ',  number ** 2)

# A for loop picking values from a list
for number in ['This', 'is', 'a', 'beautiful', 'day']:
    print(number)

# Printing lines of a exisiting files
with open("/etc/motd", 'r') as f:
    total_lines=f.readlines()
for number in total_lines:
    print(number)

# A for loop to pick keys from dictionary
test_dict = {'name': 'HG', 'age': 35, 'gender': 'male'}
for number in test_dict:
    print(number)

# A for loop for printing all dictionary values
test_dict = {'name': 'HG', 'age': 35, 'gender': 'male'}
for variable,value in test_dict.items():
    print(variable, '==>', value)

# Understanding use of break in for loop
for fruit in ['orange', 'apple', 'grape', 'melon', 'banana']:
    if fruit == 'grape':
        break
    print(fruit)

# Understanding use of continue in for loop
for fruit in ['orange', 'apple', 'grape', 'melon', 'banana']:
    if fruit == 'grape':
        continue
    print(fruit)

# A general while and problems with it
count = 0
while True:
    count += 1
    print(count, '- ', "Infinite loop")

# Inserting a break condition
count = 0
while True:
    count += 1
    print(count, '- ', "Infinite loop")
    if count == 100:
        break

# Putting a finite expression with while loop
count = 0
while count < 15:
    count += 1
    print(count, '- ', "Infinite loop")

# Putting a continue condition with while loop
count = 0
while count < 15:
    count += 1
    if (count >= 5) and (count <=10):
        continue
    print(count, '- ', "Infinite loop")