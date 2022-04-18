colors = ["red", "green", "brown"]

for color in colors:
    print(f"The color is {color}")

# when we are in the loop the variable colors exists even outside of the loop.
# the value of that variable will be the value of the last element in the loop.
print(color)  # brown

# --------- RANGE -----------
print('\n RANGE \n')

# we can create a range, which will consist of three elements
ls = list(range(3))
print(ls)  # [0,1,2]

# but we need to assign it to the list, else we will get the range function:
print(range(3))

# range ccn take starting point and ending point
ls = list(range(3, 7))
print(ls)  # [3,4,5,6]

for num in range(3, 7):
    print(num)

# get the index and the value,
ls = list(enumerate(colors))  # [(0, 'red'), (1, 'green'), (2, 'brown')]
print(ls)

for index, color in ls:
    print(F"{color} color at {index}")

# --------- RANGE -----------

# --------- LOOPING OVER DICT -----------
print('\n LOOPING OVER DICT \n')

hex_colors = {
    "Red": "#FF0000",
    "Green": "#008000",
    "Blue": "#0000FF"
}

# when we loop over the dict we get only key
for foo in hex_colors:
    print(foo)  # Red Green Blue

# if we need to get both, value and the key we must use items method
print(hex_colors.items())  # dict_items([('Red', '#FF0000'), ('Green', '#008000'), ('Blue', '#0000FF')])

for key, value in hex_colors.items():
    print(f"Hex code for the {key} color is: {value}")

# --------- LOOPING OVER DICT -----------

# --------- WHILE LOOP -----------

print('\n WHILE LOOP \n')

# we need some sort of a counter to use while loop:
counter = 0

while counter <= 5:
    print(counter)
    counter += 1

# --------- WHILE LOOP -----------

# --------- EXIT LOOPS WITH RETURN -----------
print('\n EXIT LOOPS WITH RETURN \n')


def return_target_color(target="green"):
    val = 0

    for color in colors:
        val += 1
        print(val)
        if color is target:
            return color


print(return_target_color("red"))  # 1 red
print(return_target_color())  # 1 2 green
print(return_target_color("brown"))  # 1 2 3 brown

# --------- EXIT LOOPS WITH RETURN -----------

names = ["Rose", "Max", "Nina", "Phillip"]

# --------- EXIT LOOPS WITH BREAK -----------
print('\n EXIT LOOPS WITH BREAK \n')

# "break" completely breaks out of the loop.It is for those loops where we don't need to return anything.
for name in names:
    print(f"Hello, {name}")
    if name == "Nina":
        break

# --------- EXIT LOOPS WITH BREAK -----------

# --------- EXIT LOOPS WITH CONTINUE -----------
print('\n EXIT LOOPS WITH CONTINUE \n')

# "continue" continues to the start of the loop, omitting all the code that follows it
for name in names:
    if name != "Nina":
        continue
    print(f"Hello, {name}")

# --------- EXIT LOOPS WITH CONTINUE -----------
