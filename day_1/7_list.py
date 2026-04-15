#  list 
# list is a collection of items which is ordered and changeable. It allows duplicate members.

# creating a list

my_list = [1, 2, "string", 4.0, True]
print(my_list)
# accessing elements of a list
print(my_list[0]) # to access the first element of the list
print(my_list[-1]) # to access the last element of the list

print(type(my_list)) # to check the type of the list

print()

#tuple
# tuple is a collection of items which is ordered and unchangeable. It allows duplicate members.
# creating a tuple
my_tuple = (10, 20, 30)
print(my_tuple)
# accessing elements of a tuple
print(my_tuple[0]) # to access the first element of the tuple

# list indexing
# list slicing
# list methods
# list comprehension 
# list iteration

print()

#set 
# set is a collection of items which is unordered and unindexed. It does not allow duplicate members.
# creating a set
my_set = {1, 2, 2, 3, 3, 4}
print(my_set)

print()

# dictionary
# dictionary is a collection of items which is unordered, changeable and indexed. It does not
# allow duplicate members.
# creating a dictionary
my_dict = {
    "name": "Rajan", 
    "age": 21
}
print(my_dict)