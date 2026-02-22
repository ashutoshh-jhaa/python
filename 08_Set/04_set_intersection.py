# ------------------------------------------------------------
# Python Set Intersection
# ------------------------------------------------------------

# Basic syntax (method):
# set1.intersection(iterable1, iterable2, ...)

# Basic syntax (operator):
# set1 & set2 & set3


# ------------------------------------------------------------
# 1. Intersection of Two Sets
# ------------------------------------------------------------

s1 = {"Python", "Java", "C++"}
s2 = {"C#", "Java", "C++"}

result = s1.intersection(s2)

print(result)  # {'Java', 'C++'}

# Mental Model:
# Keep ONLY elements common to ALL sets.

# Time Complexity:
# O(min(len(s1), len(s2))) average case


# ------------------------------------------------------------
# 2. Using & Operator
# ------------------------------------------------------------

s1 = {"Python", "Java", "C++"}
s2 = {"C#", "Java", "C++"}

result = s1 & s2

print(result)

# Same performance as intersection()
# Cleaner for simple set-to-set operations


# ------------------------------------------------------------
# 3. Multiple Set Intersection
# ------------------------------------------------------------

a = {1, 2, 3, 4}
b = {2, 3, 5}
c = {2, 6, 3}

result = a.intersection(b, c)
print(result)  # {2, 3}

# With operator:
result = a & b & c
print(result)


# ------------------------------------------------------------
# 4. intersection() Accepts Any Iterable
# ------------------------------------------------------------

numbers = {1, 2, 3}
scores = [2, 3, 4]

result = numbers.intersection(scores)

print(result)  # {2, 3}

# Internally converts iterable → set


# ------------------------------------------------------------
# 5. & Operator Restriction
# ------------------------------------------------------------

numbers = {1, 2, 3}
scores = [2, 3, 4]

# result = numbers & scores
# TypeError: unsupported operand type(s) for &: 'set' and 'list'

# Fix:
result = numbers & set(scores)


# ------------------------------------------------------------
# 6. Important Rules
# ------------------------------------------------------------

# 1. Returns a NEW set.
# 2. Original sets remain unchanged.
# 3. Order is not guaranteed.
# 4. Only common elements survive.
# 5. Works only with hashable elements.


# ------------------------------------------------------------
# 7. Common Mistakes
# ------------------------------------------------------------

# Mistake 1: Expecting original set to change

a = {1, 2, 3}
b = {2}

a.intersection(b)
print(a)  # still {1, 2, 3}

# Correct:
a = a.intersection(b)


# Mistake 2: Using & with non-set iterable
# Always convert iterable first.


# ------------------------------------------------------------
# 8. Key Insight
# ------------------------------------------------------------

# Intersection shrinks sets.
# It is a filtering operation:
# "Keep only elements that appear everywhere."

# Useful for:
# - Finding common skills
# - Matching tags
# - Shared permissions
