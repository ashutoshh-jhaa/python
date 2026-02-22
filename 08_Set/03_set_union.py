# ------------------------------------------------------------
# Python Set Union
# ------------------------------------------------------------

# Basic syntax (method):
# set1.union(iterable1, iterable2, ...)

# Basic syntax (operator):
# set1 | set2


# ------------------------------------------------------------
# 1. Union of Two Sets
# ------------------------------------------------------------

s1 = {"Python", "Java"}
s2 = {"C#", "Java"}

result = s1.union(s2)

print(result)  # {'Python', 'Java', 'C#'}

# Mental Model:
# Combine everything from both sets.
# Duplicates are automatically removed.

# Time Complexity:
# O(len(s1) + len(s2))


# ------------------------------------------------------------
# 2. Using | Operator
# ------------------------------------------------------------

s1 = {"Python", "Java"}
s2 = {"C#", "Java"}

result = s1 | s2

print(result)

# Important:
# | only works between sets.


# ------------------------------------------------------------
# 3. union() Accepts Any Iterable
# ------------------------------------------------------------

rates = {1, 2, 3}
ranks = [2, 3, 4]

ratings = rates.union(ranks)

print(ratings)  # {1, 2, 3, 4}

# union() internally converts iterable → set.


# ------------------------------------------------------------
# 4. | Operator Restriction
# ------------------------------------------------------------

rates = {1, 2, 3}
ranks = [2, 3, 4]

# ratings = rates | ranks
# TypeError: unsupported operand type(s) for |: 'set' and 'list'

# Fix:
ratings = rates | set(ranks)


# ------------------------------------------------------------
# 5. Multiple Set Union
# ------------------------------------------------------------

a = {1, 2}
b = {2, 3}
c = {3, 4}

result = a.union(b, c)
print(result)  # {1, 2, 3, 4}

# With operator:
result = a | b | c
print(result)


# ------------------------------------------------------------
# 6. Important Rules
# ------------------------------------------------------------

# 1. Union returns a NEW set.
# 2. Original sets remain unchanged.
# 3. Order is not guaranteed (sets are unordered).
# 4. Only hashable (immutable) elements allowed inside sets.


# ------------------------------------------------------------
# 7. Common Mistakes
# ------------------------------------------------------------

# Mistake 1: Expecting original set to change

a = {1, 2}
b = {3}

a.union(b)
print(a)  # still {1, 2}

# Use assignment if needed:
a = a.union(b)


# Mistake 2: Using | with non-set iterable
# Always convert first if needed.


# ------------------------------------------------------------
# 8. Key Insight
# ------------------------------------------------------------

# Union is a hash-based merge operation.
# Fast membership check (average O(1)) ensures uniqueness.
# Think of it as:
# "Add all elements of the second set into the first, ignoring duplicates."
