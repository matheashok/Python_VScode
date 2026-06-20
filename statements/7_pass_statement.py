# The pass Statement
# if statements cannot be empty, but if you for some reason have an if statement with no content,
#                                            put in the pass statement to avoid getting an error.

# Example : 

'''a = 33
b = 200

if b > a:
  pass'''

# The pass statement is a null operation - nothing happens when it executes. It serves as a placeholder.

# Why Use pass?
'''The pass statement is useful in several situations:

When you're creating code structure but haven't implemented the logic yet
When a statement is required syntactically but no action is needed
As a placeholder for future code during development
In empty functions or classes that you plan to implement later'''

# pass in Development
# During development, you might want to sketch out your program structure before implementing the details.
#                                          The pass statement allows you to do this without syntax errors.

# Example : Placeholder for future implementation:

'''age = 16

if age < 18:
  pass # TODO: Add underage logic later
else:
  print("Access granted")'''

# pass vs Comments
# A comment is ignored by Python, but pass is an actual statement that gets executed 
# (though it does nothing). You need pass where Python expects a statement, not just a comment.

# Example : This will cause an error (empty code block):

'''score = 85

if score > 90:
  # This is excellent
# This will raise an IndentationError'''

# Example : This works correctly with pass:

'''score = 85

if score > 90:
  pass # This is excellent
print("Score processed")'''

# pass with Multiple Conditions
# You can use pass in any branch of an if-elif-else statement.

# Example : Using pass in different branches:

'''value = 50

if value < 0:
  print("Negative value")
elif value == 0:
  pass # Zero case - no action needed
else:
  print("Positive value")'''

# pass in Other Contexts
# While we focus on pass with if statements here, it's also commonly used with loops, functions,
#                                                                                   and classes.

# Example : Using pass with functions:

'''def calculate_discount(price):
  pass # TODO: Implement discount logic

# Function exists but doesn't do anything yet'''


