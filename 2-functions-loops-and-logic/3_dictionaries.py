# dictionaries store key value pairs, they are mutable but the keys can only be immutable. Dict keys can be tuples,
# string, numbers or anything that is hashable. Because when we access a specific property of a Dict we are comparing
# the hashes.

my_dict = {}
print(type(my_dict))  # <class 'dict'>

my_dict = {"one": 1, "two": 2}
print(my_dict)

# accessing the values
print(my_dict["one"])

# if we will try to access value that doesn't exist we will get KeyError, to avoid it we can use get method
print(my_dict.get('three'))  # None

# if the jey doesn't exist we can return the default value by passing it as a second argument into get method
print(my_dict.get('three', 3))  # 3

# update items in a Dict
my_dict['one'] = 1.0
my_dict['two'] = 2.0
print(my_dict)  # {'one': 1.0, 'two': 2.0}

# add items to a Dict
my_dict['three'] = 3.0
print(my_dict)  # {'one': 1.0, 'two': 2.0, 'three': 3.0}

# discard item from a Dict
my_dict.pop('three')
print(my_dict)  # {'one': 1.0, 'two': 2.0}

# combined two Dicts
my_dict_3 = {'three': 3.0}
my_dict.update(my_dict_3)
print(my_dict)  # {'one': 1.0, 'two': 2.0, 'three': 3.0}

# working with Dict values
print(my_dict.keys())  # dict_keys(['one', 'two', 'three'])
print(my_dict.values())  # dict_values([1.0, 2.0, 3.0])
print(my_dict.items())  # dict_items([('one', 1.0), ('two', 2.0), ('three', 3.0)])

