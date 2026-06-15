# Check if the string ends with a punctuation sign (.):

'''txt = "Hello, welcome to my world."

x = txt.endswith(".")

print(x)'''

# Definition and Usage
# The endswith() method returns True if the string ends with the specified value,
#  otherwise False.

# Syntax : string.endswith(value, start, end)

# Parameter Values
# value : Required. The value to check if the string ends with. 
#         This value parameter can also be a tuple, then the method returns true 
#         if the string ends with any of the tuple values.
# start : Optional. An Integer specifying at which position to start the search
# end : Optional. An Integer specifying at which position to end the search

# Check if the string ends with the phrase "my world.":

'''txt = "Hello, welcome to my world."

x = txt.endswith("my world.")

print(x)'''

# Check if position 5 to 11 ends with the phrase "my world.":

'''txt = "Hello, welcome to my world."

x = txt.endswith("my world.", 5,11)

print(x)'''

# Check if the string ends with either the phrase "world." or "castle.":

'''txt = "Hello, welcome to my castle."

x = txt.endswith(("world.", "castle."))

print(x)'''

