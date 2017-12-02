# Your assignment is to get the last line to print without changing any
# of the code below. Instead, wrap each line that throws an error in a
# try/except block.

try: 
    print("Infinity looks like + " + str(10 / 0) + ".")
except ZeroDivisionError:
    print("You can't divide by zero you jackass")
try:
    print("I think her name was + " + name + "?")
except NameError:
    print("You need a name you jackass")
try:
    print("Your name is a nonsense number. Look: " + int("Gabriel"))
except ValueError: 
    print("Names are not integers, you jackass.")

print("You made it through the gauntlet--the message survived!")

#try:
    #blahgajg
#except KeyError