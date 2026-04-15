# write a python program to find the sum of digits of a given number

num = int(input("Enter a number: "))
sum = 0
while(num > 0):
    digit = num % 10 # to get the last digit of the number
    sum += digit # to add the last digit to the sum
    num = num // 10 # to remove the last digit of the number

print("The sum of digits is:", sum) # to print the sum of digits