# files with the extension of .pyc are compiled files that we shouldn't commit to avoid some issues
# we can delete them using the following command: `find . name "*.pyc" -delete`
# don't forget to add the following to the .gitignore: *.pyc

# whenever there is a very large list or other type that we are printing we can ise pprint and it will add line breaks
from pprint import pprint

pprint([2,123423,42,424,2,42,4,234,234,32,43,23,42,43,45,345,356,46,465,4,624,24,24,2,42,34])

