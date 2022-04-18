names = ["Levan", "Kostas", "Ona Marija"]
my_list = []

for name in names:
    my_list.append(len(name))

print(my_list)  # [5,6,10]

# we can get the same result using the list comprehension, we define what we do with the element in the beginning
my_list_with_comprehension = [len(name) for name in names]

print(my_list == my_list_with_comprehension)  # True

# we can have conditional statements in list comprehensions, we define conditions at the end
print([name for name in names if len(name) % 2 == 0])  # ['Kostas', 'Ona Marija']

# splitting a string
long_str = "Levan, Kostas, Ona Marija"

split_long_str = long_str.split(',')
print(split_long_str)  # ['Levan', ' Kostas', ' Ona Marija']

# joining a list
joined_list = " - ".join(split_long_str)
print(joined_list)  # Levan -  Kostas -  Ona Marija

# joining a list with comprehension
my_nums = [1, 2, 3]

print(", ".join(str(num * 2) for num in my_nums))  # "2, 4, 6"

# generators comprehension: Generator is like an object that we can iterate over. Generator only knows where
# it is and how to get the next value on demand, without generated the whole list all at once.
gen_comp = (x ** 2 for x in range(10) if x % 2 == 0)
print(type(gen_comp))  # <class 'generator'>
print(gen_comp)  # <generator object <genexpr> at 0x10293ef90>

# we don't need to make a list from the generator, we can loop over it and make with it's element whatever we need.

for item in gen_comp:
    print(item)  # 0 4 16 36 64

# generator is not stored in the memory, if we have used it once it will be exhausted.

for item in gen_comp:
    print(item)  # won't print anything
