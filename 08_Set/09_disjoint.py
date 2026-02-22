# ------------------------------------------------------------
# Python isdisjoint() – Disjoint Sets
# ------------------------------------------------------------

# Basic syntax:
# set_a.isdisjoint(iterable)


# ------------------------------------------------------------
# 1. What are Disjoint Sets?
# ------------------------------------------------------------

# Two sets are disjoint if:
# They have NO common elements.

# Equivalent definition:
# Intersection is empty set.

# Mental Model:
# "Do these sets share anything?"


# ------------------------------------------------------------
# 2. Basic Example
# ------------------------------------------------------------

odd_numbers = {1, 3, 5}
even_numbers = {2, 4, 6}

result = odd_numbers.isdisjoint(even_numbers)
print(result)  # True


# ------------------------------------------------------------
# 3. Not Disjoint Case
# ------------------------------------------------------------

letters = {"A", "B", "C"}
alphanumerics = {"A", 1, 2}

result = letters.isdisjoint(alphanumerics)
print(result)  # False

# Because 'A' exists in both.


# ------------------------------------------------------------
# 4. Accepts Any Iterable
# ------------------------------------------------------------

letters = {"A", "B", "C"}

result = letters.isdisjoint([1, 2, 3])
print(result)  # True

# Internally converts iterable → set


# ------------------------------------------------------------
# 5. Equivalent Logic (Manual Check)
# ------------------------------------------------------------

a = {1, 2, 3}
b = {4, 5}

# Equivalent to:
print(a.intersection(b) == set())  # True

# But isdisjoint() is faster and cleaner.


# ------------------------------------------------------------
# 6. Performance
# ------------------------------------------------------------

# Time Complexity:
# O(min(len(set_a), len(set_b))) average case

# Stops early as soon as common element is found.
# Efficient for large sets.


# ------------------------------------------------------------
# 7. Important Rules
# ------------------------------------------------------------

# 1. Returns True if NO common elements.
# 2. Returns False if at least ONE common element exists.
# 3. Does NOT modify original sets.
# 4. Order does not matter.


# ------------------------------------------------------------
# 8. Common Mistakes
# ------------------------------------------------------------

# Mistake 1: Confusing with subset

a = {1, 2}
b = {3, 4}

print(a.isdisjoint(b))  # True
# Does NOT mean subset relationship.


# Mistake 2: Thinking empty set breaks it

a = set()
b = {1, 2, 3}

print(a.isdisjoint(b))  # True

# Empty set is disjoint with every set.


# ------------------------------------------------------------
# 9. Key Insight
# ------------------------------------------------------------

# isdisjoint() is the fastest way to check:
# "Do these sets overlap?"

# If you only care about overlap,
# use isdisjoint() instead of intersection().
