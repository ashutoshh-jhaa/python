# ------------------------------------------------------------
# Data Structures: Tuple
# ------------------------------------------------------------
# A tuple is an ordered, immutable collection of items


# ------------------------------------------------------------
# 1. Creating Tuples
# ------------------------------------------------------------

rgb = ("red", "green", "blue")
print(rgb)


# ------------------------------------------------------------
# 2. Accessing Elements
# ------------------------------------------------------------

print(rgb[0])  # red
print(rgb[1])  # green
print(rgb[2])  # blue

# Negative indexing
print(rgb[-1])  # blue


# ------------------------------------------------------------
# 3. Immutability (Important)
# ------------------------------------------------------------

# Tuples cannot be modified

# This will cause an error:
# rgb[0] = 'yellow'
# TypeError: 'tuple' object does not support item assignment


# ------------------------------------------------------------
# 4. Single Element Tuple
# ------------------------------------------------------------

t1 = (3,)
print(type(t1))  # tuple

t2 = 3
print(type(t2))  # int (not a tuple)


# ------------------------------------------------------------
# 5. Reassignment (Allowed)
# ------------------------------------------------------------

colors = ("red", "green", "blue")
print(colors)

# You cannot modify, but you can reassign
colors = ("cyan", "magenta", "yellow", "black")
print(colors)


# ------------------------------------------------------------
# Important Notes
# ------------------------------------------------------------
# - Tuple is immutable (cannot change elements)
# - Maintains order
# - Allows duplicates
# - Can store mixed data types


# ------------------------------------------------------------
# Key Insight (Very Important)
# ------------------------------------------------------------
# Tuple is immutable, but it still stores references

a = ([1, 2], [3, 4])  # tuple containing lists

a[0].append(100)
print(a)
# ([1, 2, 100], [3, 4])


# Why this works:
# - Tuple itself is immutable
# - But objects inside it (lists) are mutable


# ------------------------------------------------------------
# Summary
# ------------------------------------------------------------
# - Tuple = immutable list
# - Use () instead of []
# - Cannot modify elements
# - But inner mutable objects can still change
