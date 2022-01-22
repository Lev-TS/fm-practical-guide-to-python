# sets are mutable data types that allow you to store only immutable data types (e.g. int, str, tuples, etc).
# In contrast with tuples Sets are not sorted. Set's can contain only unique items in them. As a result they re very
# fast.

# sets are wrapped in curly braces
my_set = {1, 'Levan', 3, ('student', 'tsu', 3.8)}
print(type(my_set))  # <class 'set'>

# if we assign empty curly braces to the variable the type will be dict instead of set
my_set = {}
print(type(my_set))  # <class 'dict'>

# if we want to create an empty set we should use the constructor
my_set = set()
print(type(my_set))  # <class 'set'>

# if we pass two or more similar items in the set, it will hold only one item
my_set = {1, 1, 1, 2}
print(my_set)  # {1. 2}

# if we want to remove duplicates from the list we can pass it into set constructor
my_list = ['Levan', 'Levan', 36, 36]
my_set = set(my_list)
print(my_set)  # {36, Levan}

# a quick way to check if a variable or a value is mutable is to use hash method. Only not mutable types are hashable
print(hash(1))
print(hash('Levan'))
print(hash(('student', 'tsu', 3.8)))
# hash([]) hashing a mutable type will throw TypeError

# sets don't have an order. If a print a set twice, there is not guarantee
# the items will come up in the same order.
my_set = {1, 'Levan', 3, ('student', 'tsu', 3.8)}
print(my_set)  # {3, 1, 'Levan', ('student', 'tsu', 3.8)}
print(my_set)  # {('student', 'tsu', 3.8), 1, 3, 'Levan'}
# this is why set are not indexed. my_set[0] will raise the TypeError

# we can add/remove items to sets
my_set = set()
my_set.add('Levan')
my_set.add('Kostas')
my_set.add('Tsutskiridze')
my_set.discard('Levan')
print(my_set) # {'Tsutskiridze', 'Kostas'}

# we can combine sets
my_set_1 = {'Tsutskiridze', 'Kostas'}
my_set_2 = {('student', 'tsu', 3.8), 1, 3, 'Levan'}

my_set_1.update(my_set_2)
print(my_set_1)

