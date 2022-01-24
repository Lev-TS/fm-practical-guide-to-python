# arguments with default value should always be at the end
def add_numbers(x, y, z=1):
    return x + y + z


# parameters passed should be in order
result = add_numbers(2, 3)
print(result)

# we can provide named parameters and then the order doesn't matter. but all should be named
result = add_numbers(z=1, y=1, x=2)
print(result)


def create_query(language="JavaScript", num_stars=10, sort='desc'):
    return f"language: {language}, num_stars: {num_stars}, sort: {sort}"


print(create_query())
print(create_query(language="Python"))
print(create_query(num_stars=9))
print(create_query(sort="asc"))


# don't use mutable types as default arguments!! They get declared once and each time we call the function we reuse it
def do_something(my_list=[]):
    my_list.append('something')
    return my_list


print(do_something())  # ['something']
print(do_something())  # ['something', 'something']
print(do_something())  # ['something', 'something', 'something']


# instead we can do something like this
def do_something(my_list=None):
    if my_list is None:
        my_list = []
    my_list.append('something')
    return my_list


print(do_something())  # ['something']
print(do_something())  # ['something']
print(do_something())  # ['something']

# arguments in function are passed by value not reference.
name = "Levan"


def change_name(name):
    name = "Konstas"
    print(f"name inside of a func is: {name}")


change_name(name)
print(f"name outside of a func is: {name}")
