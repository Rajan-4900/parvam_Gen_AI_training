# looping - to avoid repetition of code

# for loop - iterate over a sequence (list, string, range)
# for loop

# syntax for var_name in range(start, stop, step):

#print numbers from 0 to 9
for i in range(0,10,1):
    print(i,end=" ") # prints numbers from 0 to 9

print()

# print even numbers from 0 to 10
for j in range(0,10,1):
    print(j*2, end=" ")

# printing the table user provided
num = int(input("Enter a number: "))
for k in range(1,11,1):
    print(num, "*", k, "=", num*k)