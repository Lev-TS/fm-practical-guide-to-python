# 1. Course Website

https://practical.learnpython.dev/00_course_intro/

# 2. Basics

- Create virtual environment using built in venv:
  - `python3 -m venv <your_env_name>`
- Activate virtual env
  - `source <your_env_name>/bin/activate`
- Run the code via
  - activate virtual env
  - run: `python <file-name.py>`
- Deactivate virtual env
  - `deactivate`

# 3. Variables and Data Types

## Useful methods in REPL

1. `type()`: sort of `typeof` you pass in the value or var you want to check

```python
type(1) # <class 'int'>
type('value') # <class 'str'>
```

2. `dir()`: return all the method that are available on the passed in parameter.

3. `help()`: returns info about the passed in class.

## Numbers

- three number types:
  1. `int` e.g. `1` or `2`
  2. `float` e.g. `1.0` or `2.0` (edges: `0.` or `1.` is also float)
  3. `complex` should end on `j` e.g. `42j`
- concatenate str and int: `"hi " + str(5) + " times"`
- all the operators from JS ar valid here as well
- the main difference is the way division is happening:

```python
25 / 5 # returns float 5.0
25 // 5 # returns int 5
```

- we also have to the power operator `**`

```python
x=2
y=3
x**y # returns int 8
```

- There are three most helpful built in methods: `min, max, round`

```python
min(1, 10, -3) # returns -3, the smallest passed value
max(1, 10, -3) # returns 10, the largest passed value
round(3.5) # returns 4, rounds up
round(3.4) # returns 3, rounds down
```

- under the hood booleans have int values True=1 and False=0, so we can technically use operators with them, but never do this.

```python
# NEVER DO THIS
True + True # returns 2
True + False # returns 1
```

## Strings

- single or double quotes
  - we can do either `"don't"` or `'don\'t'`
- very long string

```python
very_long_string = """
this is a very
long string
that takes multiple lines
""" # returns: '\n  this is a very\n  long string \n  that takes multiple lines\n'
```

- `\n` = new line
- `\t` = tab
- concatenation
  - string w/ strings: `"good" + " and " + "ugly"`
  - string w/ number: `"good" + str(10)`
- interpolation

```python
x="book"
f"very good {x}"
```

- replace

```python
x="book"
x.replace("b", "h") # returns "hook" but doesn't reassign the x's value, which will remain "book"
```

## List

- We can make lists in various ways

```python
x=list() # returns []
y=[1,2,3]
y[0] # lists are zero indexed so y[0] returns 1
y[3] # will raise IndexError: list index out of range
y[1]=10 # list is mutable
y[3] # this will error
```

- list methods

```python
y=[1,2,3]

a = sorted(y) # returns the ascending sorted list, doesn't mutate y
b = sorted(y, reverse=true) # returns descending sorted list
c = y + [1, 2, 3] # appends without mutations

y.sort() # will mutate y
y.reverse() # descending order
y.append(0) # sort of push
y.insert(0, 100) # insert 100 at index 0

1 in y # will return True if y has element with the value of 1

#check other methods in REPL
dir(list)

```
