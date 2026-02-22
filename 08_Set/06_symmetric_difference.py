# ------------------------------------------------------------
# Python Symmetric Difference
# ------------------------------------------------------------

# Basic syntax (method):
# set1.symmetric_difference(iterable)

# Basic syntax (operator):
# set1 ^ set2


# ------------------------------------------------------------
# 1. Symmetric Difference of Two Sets
# ------------------------------------------------------------

s1 = {"Python", "Java", "C++"}
s2 = {"C#", "Java", "C++"}

result = s1.symmetric_difference(s2)

print(result)  # {'Python', 'C#'}

# Mental Model:
# Elements in either set
# BUT NOT in both

# Equivalent to:
# (A - B) ∪ (B - A)

# Time Complexity:
# O(len(s1) + len(s2))


# ------------------------------------------------------------
# 2. Using ^ Operator
# ------------------------------------------------------------

s1 = {"Python", "Java", "C++"}
s2 = {"C#", "Java", "C++"}

result = s1 ^ s2
print(result)

# Cleaner for set-to-set operations
# Same performance as method


# ------------------------------------------------------------
# 3. Multiple Set Symmetric Difference
# ------------------------------------------------------------

a = {1, 2, 3}
b = {3, 4}
c = {4, 5}

result = a ^ b ^ c
print(result)

# Note:
# ^ is left-associative:
# (a ^ b) ^ c


# ------------------------------------------------------------
# 4. symmetric_difference() Accepts Iterables
# ------------------------------------------------------------

scores = {7, 8, 9}
ratings = [8, 9, 10]

new_set = scores.symmetric_difference(ratings)
print(new_set)  # {7, 10}

# Internally converts iterable → set


# ------------------------------------------------------------
# 5. ^ Operator Restriction
# ------------------------------------------------------------

scores = {7, 8, 9}
ratings = [8, 9, 10]

# new_set = scores ^ ratings
# TypeError: unsupported operand type(s) for ^: 'set' and 'list'

# Fix:
new_set = scores ^ set(ratings)


# ------------------------------------------------------------
# 6. Important Rules
# ------------------------------------------------------------

# 1. Returns a NEW set.
# 2. Original sets remain unchanged.
# 3. Order is not guaranteed.
# 4. Keeps elements that appear ODD number of times
#    when chaining multiple ^ operations.


# ------------------------------------------------------------
# 7. Common Mistakes
# ------------------------------------------------------------

# Mistake 1: Confusing with union
# Union keeps everything.
# Symmetric difference removes common elements.

a = {1, 2, 3}
b = {3, 4}

print(a | b)  # {1, 2, 3, 4}
print(a ^ b)  # {1, 2, 4}


# Mistake 2: Expecting original set to change

a = {1, 2, 3}
b = {3}

a.symmetric_difference(b)
print(a)  # unchanged


# ------------------------------------------------------------
# 8. In-Place Version
# ------------------------------------------------------------

a = {1, 2, 3}
b = {3, 4}

a.symmetric_difference_update(b)
print(a)  # {1, 2, 4}


# ------------------------------------------------------------
# 9. Key Insight
# ------------------------------------------------------------

# Symmetric Difference = XOR logic for sets.

# Think:
# Keep elements that are different between sets.

# Binary analogy:
# 1 ^ 1 = 0
# 1 ^ 0 = 1
# 0 ^ 1 = 1
