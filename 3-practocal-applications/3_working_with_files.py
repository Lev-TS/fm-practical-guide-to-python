# open a file for reading
my_file = open("static-files/my_file.txt")

# open a file for reading and writing
# This will replace any existing file
my_file_w = open("static-files/my_file.txt", "w")

# open a file for reading and writing
# This will append to the end of any existing file
my_file_a = open("static-files/my_file.txt", "a")

# when we open a file we should always close it, otherwise the file will end up in a useless state.
# This is concerning because if our app fails before we close the file, the file will remain in this state.
# We can use something similar to try ... finally block to ensure that the logic is handled automatically
with open("static-files/my_file.txt") as my_file_with_context_manager:
    content = my_file_with_context_manager.read()


