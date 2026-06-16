# Operator precedence describes the order in which operations are performed.

# Parentheses has the highest precedence, meaning that expressions inside parentheses must be evaluated first:

'''print((6 + 3) - (6 + 3))'''


# Multiplication * has higher precedence than addition +, and therefore multiplications
#                                                    are evaluated before additions:

'''print(100 + 5 * 3)'''

# If two operators have the same precedence, the expression is evaluated from left 
#                                                                         to right.
# Example : Addition + and subtraction - has the same precedence, and therefore we
#                                        evaluate the expression from left to right:

'''print(5 + 4 - 7 + 3)'''

