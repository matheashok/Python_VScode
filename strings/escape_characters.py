# Escape Character
# To insert characters that are illegal in a string, use an escape character.
# An escape character is a backslash \ followed by the character you want to insert.
# An example of an illegal character is a double quote inside a string that is surrounded by double quotes:
# You will get an error if you use double quotes inside a string that is surrounded by double quotes:

'''txt = "We are the so-called "Vikings" from the north."
print(txt)'''

# To fix this problem, use the escape character \":
# The escape character allows you to use double quotes when you normally would 
# not be allowed:

'''txt = "We are the so-called \"Vikings\" from the north."
print(txt)'''

# Escape Characters
# Other escape characters used in Python:

# Single Quote
'''txt = 'It\'s alright.'
print(txt) '''

# Backslash
'''txt = "This will insert one \\ (backslash)."
print(txt) '''

# New Line
'''txt = "Hello\nWorld!"
print(txt) '''

# Carriage Return
'''txt = "Hello\rWorld!"
print(txt) '''

# Tab
'''txt = "Hello\tWorld!"
print(txt) '''

# Backspace
#This example erases one character (backspace):
'''txt = "Hello \bWorld!"
print(txt) '''

# 	Form Feed



# Octal value
#A backslash followed by three integers will result in a octal value:
'''txt = "\110\145\154\154\157"
print(txt) '''

# Hex value
#A backslash followed by an 'x' and a hex number represents a hex value:
'''txt = "\x48\x65\x6c\x6c\x6f"
print(txt)'''

