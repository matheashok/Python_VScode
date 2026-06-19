# Python frozenset
# frozenset is an immutable version of a set.
# Like sets, it contains unique, unordered, unchangeable elements.
# Unlike sets, elements cannot be added or removed from a frozenset.
# Creating a frozenset : Use the frozenset() constructor to create a frozenset from any iterable.

# Example : Create a frozenset and check its type:

'''x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))'''

# Frozenset Methods
# Being immutable means you cannot add or remove elements. However, frozensets support all 
#                                                          non-mutating operations of sets.

# copy() : Returns a shallow copy
'''fs = frozenset({1, 2, 3})
cp = fs.copy()
print(fs)
print(cp)'''

# difference() : Returns a new frozenset with the difference
'''a = frozenset({1, 2, 3, 4})
b = frozenset({3, 4, 5})
print(a.difference(b))
print(a - b)'''

# intersection() : Returns a new frozenset with the intersection
'''a = frozenset({1, 2, 3, 4})
b = frozenset({3, 4, 5})
print(a.intersection(b))
print(a & b)'''

# isdisjoint() : Returns True if there is NO intersection between two frozensets
'''a = frozenset({1, 2})
b = frozenset({3, 4})
c = frozenset({2, 3})
print(a.isdisjoint(b))
print(a.isdisjoint(c))'''

# issubset() : Returns True if this frozenset is a (proper) subset of another
'''a = frozenset({1, 2})
b = frozenset({1, 2, 3})
print(a.issubset(b))
print(a <= b)
print(a < b)'''

# issuperset() : Returns True if this frozenset is a (proper) superset of another
'''a = frozenset({1, 2, 3})
b = frozenset({1, 2})
print(a.issuperset(b))
print(a >= b)
print(a > b)'''

# symmetric_difference() : Returns a new frozenset with the symmetric differences
'''a = frozenset({1, 2, 3})
b = frozenset({3, 4, 5})
print(a.symmetric_difference(b))
print(a ^ b)'''

# union() : Returns a new frozenset containing the union
'''a = frozenset({1, 2})
b = frozenset({2, 3})
print(a.union(b))
print(a | b)'''



