# Importing the needed modules
from sys import platform as pf
from os import system

# Find the system
clearingCommand = 'NULL'
if pf == "linux" or pf == "linux2" or pf == "darwin":
    clearingCommand = 'clear'
elif pf == "win32":
    clearingCommand = 'cls'

# Functions
def clear():
    system(clearingCommand)