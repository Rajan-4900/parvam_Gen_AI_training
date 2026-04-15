# Program to print all numbers from 1 to 100 that are multiples of 5
for i in range(1, 101):
    if i % 5 == 0:
        print(i, end=' ')

print()

# Program to check if a number is a palindrome
num = int(input("Enter a number: "))
original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if original == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")

print()

# Program to count the number of digits in a number
num = int(input("Enter a number: "))
count = 0

while num > 0:
    count += 1
    num = num // 10

print("Number of digits:", count)

print()

# Program to check if a number is prime
num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime Number")
else:
    print("Not Prime")

print()

# Program to find the sum of digits of a number
num = int(input("Enter a number: "))
sum_digits = 0

while num > 0:
    digit = num % 10
    sum_digits += digit
    num = num // 10

print("Sum of digits:", sum_digits)