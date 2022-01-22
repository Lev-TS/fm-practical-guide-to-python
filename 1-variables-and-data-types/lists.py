# dir(list)
# help(list.append)

my_list = ["Hello", "Hi"]
print(type(my_list))

print(len(my_list))  # 2
my_list.append("Hola")  # my_list = ["Hello", "Hi", "Hola"]
print(len(my_list))  # 3
my_list.pop()  # my_list = ["Hello", "Hi"]
print(my_list)

my_list[0] = 'hola'

# no mutation
my_list_sorted = sorted(my_list)
print(my_list_sorted)  # ['Hi', 'hola']
print(my_list)  # ['hola', 'Hi']

# with mutation
my_list.sort()
print(my_list) # ['Hi', 'hola']

