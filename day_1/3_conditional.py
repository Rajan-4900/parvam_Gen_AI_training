# Conditional Statements in Python

# if statement --> to check a single condition
a = int(input("Enter a Value : ")) # Taking input from the user and converting it to an integer
print(a)

print(type(a)) # Checking the type of the variable 'a'
if a > 5:
    print("The number is greater than 5") # This block will execute if the condition is true


# if-else statement --> to check two conditions
b = int(input("Enter b value :"))
print(b)
if b > 10:
    print("The number is greater than 10") # This block will execute if the condition is true
else:
    print("The number is not greater than 10") # This block will execute if the condition is false

    
# if-elif-else statement --> to check multiple conditions
c = int(input("Enter c value :"))
print(c)
if c > 5:
    print("The number is greater than 5") # This block will execute if the condition is true
elif c == 5:
    print("The number is equal to 5") # This block will execute if the first condition is false and this condition is true
elif c == 0:
    print("The number is equal to 0") # This block will execute if the first two conditions are false and this condition is true
else:
    print("The number is less than 5") # This block will execute if both the above conditions are false