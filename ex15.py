# From sys means use a package, import argv means use a module.
from sys import argv
#Asking the user to state the filename.
script, filename = argv
#Using the command open to show the file in the script.
txt = open(filename)
#Printing a string with the filename given,
print "Here's you file %r:" % filename
#???
print txt.read()
#
print "Type the filename again:"
#
file_again = raw_input("> ")
#
txt_again = open(file_again)
#
print txt_again.read()
