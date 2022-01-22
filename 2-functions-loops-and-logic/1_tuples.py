# are immutable
# have order

my_tup = ()
print(type(my_tup))  # <class 'tuple'>

# tricky thing is that if tuple has only one element without comma, it won't be tuple type

my_tup = ('hi')
print(type(my_tup))  # <class 'str'>

# if we want to have only one element in the tuple we should add comma after it
my_tup = ('hi',)
print(type(my_tup))  # <class 'tuple'>

# we can access items like in case of lists
student = ('Kostas', 4, 'kindergarten')
print(student[0])  # Kostas

# can't mutate tuple
# student[0] = "Elene" -> will throw type error

# we can sort of destructure tuple. The number of arguments on the left hand side should match
# number of items in the tuple. This works with lists as well but we shouldn't use because those
# are mutable and we never know what will change.
name, age, school = student
print(name)  # 'kostas'
print(age)  # 8
print(school)  # 'kindergarten'

# if we don't care to get an item from the tuple, the common practice is to use the underscore.
name, _, _ = student

