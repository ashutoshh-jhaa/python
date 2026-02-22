# ------------------------------------------------------------
# Python issuperset() and Superset Operators
# ------------------------------------------------------------

# Basic syntax (method):
# set_a.issuperset(set_b)

# Superset operator:
# set_a >= set_b

# Proper superset operator:
# set_a > set_b


# ------------------------------------------------------------
# 1. What is a Superset?
# ------------------------------------------------------------

# Set A is a superset of Set B if:
# Every element of B exists in A.

# If A == B → still a superset.
# If A != B → A is a proper superset of B.

# Mental Model:
# "Does A fully contain B?"


# ------------------------------------------------------------
# 2. Using issuperset()
# ------------------------------------------------------------

numbers = {1, 2, 3, 4, 5}
scores = {1, 2, 3}

print(numbers.issuperset(scores))  # True

# A set is always a superset of itself

print(numbers.issuperset(numbers))  # True

# Not superset case

print(scores.issuperset(numbers))  # False


# ------------------------------------------------------------
# 3. Using >= Operator (Superset)
# ------------------------------------------------------------

numbers = {1, 2, 3, 4, 5}
scores = {1, 2, 3}

print(numbers >= scores)  # True
print(numbers >= numbers)  # True

# Equivalent to issuperset()


# ------------------------------------------------------------
# 4. Using > Operator (Proper Superset)
# ------------------------------------------------------------

numbers = {1, 2, 3, 4, 5}
scores = {1, 2, 3}

print(numbers > scores)  # True
print(numbers > numbers)  # False

# Proper superset means:
# - Must contain all elements
# - Must NOT be equal


# ------------------------------------------------------------
# 5. Important Rules
# ------------------------------------------------------------

# 1. >= checks superset (allows equality).
# 2. > checks proper superset (no equality).
# 3. A set is always a superset of itself.
# 4. Order does not matter.


# ------------------------------------------------------------
# 6. Performance
# ------------------------------------------------------------

# Time Complexity:
# O(len(set_b)) average case

# Python checks:
# For each element in set_b,
# membership in set_a (O(1) average).


# ------------------------------------------------------------
# 7. Relationship with Subset
# ------------------------------------------------------------

# A >= B  is equivalent to  B <= A
# A > B   is equivalent to  B < A

a = {1, 2, 3}
b = {1, 2}

print(a >= b)  # True
print(b <= a)  # True


# ------------------------------------------------------------
# 8. Common Mistakes
# ------------------------------------------------------------

# Mistake 1: Confusing direction

a = {1, 2}
b = {1, 2, 3}

print(a >= b)  # False
print(b >= a)  # True


# Mistake 2: Expecting > to allow equality

a = {1, 2}

print(a > a)  # False
print(a >= a)  # True


# ------------------------------------------------------------
# 9. Key Insight
# ------------------------------------------------------------

# Superset is containment in reverse direction.

# Think:
# A >= B  →  "B fits inside A"

# Opposite concept:
# Subset (<=)
