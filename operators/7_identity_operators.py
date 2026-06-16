#  Identity operators are used to compare the objects, not if they are equal, 
# but if they are actually the same object, with the same memory location:

# operator : The is operator returns True if both variables point to the same object:

'''x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z) # returns True because z is the same object as x
print(x is y) # returns False because x is not the same object as y, 
#                   even if they have the same content
print(x == y) # to demonstrate the difference betweeen "is" and "==": 
#                    this comparison returns True because x is equal to y'''



# Example : The is not operator returns True if both variables do not point to the same object:

'''x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is not z)
# returns False because z is the same object as x

print(x is not y)
# returns True because x is not the same object as y, 
#                   even if they have the same content

print(x != y)
# to demonstrate the difference betweeen "is not" and "!=": 
#   this comparison returns False because x is equal to y'''

# Difference Between is and ==
##      is - Checks if both variables point to the same object in memory
#       == - Checks if the values of both variables are equal

'''x = [1, 2, 3]
y = [1, 2, 3]

print(x == y)
print(x is y)'''

