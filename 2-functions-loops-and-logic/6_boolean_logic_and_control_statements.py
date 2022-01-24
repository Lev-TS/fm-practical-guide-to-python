# use bool() method to find out the truthy-ness of a value

# Falsy
print(bool(0))  # False
print(bool(-0))  # False
print(bool([]))  # False
print(bool({}))  # False
print(bool(()))  # False
print(bool(None))  # False

# Truthy
print(bool(3 - 10))  # True
print(bool((3, 10)))  # True
print(bool({3, 10}))  # True
print(bool([3, 10]))  # True
print(3 < 4)  # True
print(1 == 1)  # True
print(1 != 2)  # True

# referential vs value equality
my_list_1 = [1, 2, 3]
my_list_2 = [1, 2, 3]
my_list_3 = my_list_1

print(my_list_1 == my_list_2)  # True, `==` operator checks if the values are the same
print(my_list_1 == my_list_3)  # True
print(my_list_2 == my_list_3)  # True

print(my_list_1 is my_list_2)  # False, `is` operator checks if the referential equality is the same
print(my_list_1 is my_list_3)  # True
print(my_list_2 is my_list_3)  # False

# don't use value equality to find out if a value is True
a = True
b = None
c = []

print(a is True)  # True
print(b is None)  # True
print(c is not None)  # True

# other keywords are 'and', 'or', 'not'
print(True and True)  # True
print(True and False)  # False
print(True and None)  # None
print(False and None)  # False
print(None and False)  # None

print(not True)  # False
print(not False)  # True
print(not None)  # True

print(True or None)  # True
print(True or False)  # True
print(None or False)  # False

# conditionals
if True:
    print('Truthy')  # Truthy

a = []

if a:
    print("Hi")
else:
    print("Hello")  # Hello

