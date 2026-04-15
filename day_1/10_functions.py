# functions in Python

"""
 def fun_name(parameters):
        # function body

1. function taking parameters and returning a value
2. function taking parameters and not returning a value (void function)
3. function not taking parameters and returning a value
4. function not taking parameters and not returning a value (void function)
"""

# function example --> taking parameters and returning a value
def add(a,b):
    return a + b
#print(add(5, 3))  # Output: 8
result = add(5, 3)
print("taking parameters and returning a value:", result)  # Output: 8


# function example --> taking parameters and not returning a value (void function)
def greet(name):
    print("taking parameters and not returning a value:", name)
greet("Rajan")

# function example --> not taking parameters and returning a value
def get_number():
    return 10
num = get_number()
print("not taking parameters and returning a value:", num)


# function example --> not taking parameters and not returning a value (void function)
def show_message():
    print("not taking parameters and not returning a value: Welcome!")
show_message()
