# Split a string into a list where each line is a list item:

'''txt = "Thank you for the music\nWelcome to the jungle"

x = txt.splitlines()

print(x)'''

# Definition and Usage
# The splitlines() method splits a string into a list. The splitting is done at line
#                                                                            breaks.
# Syntax : string.splitlines(keeplinebreaks)
# Parameter Values
# keeplinebreaks : Optional. Specifies if the line breaks should be included (True), 
#                                           or not (False). Default value is False

# Split the string, but keep the line breaks:

'''txt = "Thank you for the music\nWelcome to the jungle"

x = txt.splitlines(True)

print(x)'''

