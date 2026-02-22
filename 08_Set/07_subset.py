# ------------------------------------------------------------
# Python issubset() and Subset Operators
# ------------------------------------------------------------

# Basic syntax (method):
# set_a.issubset(set_b)

# Subset operator:
# set_a <= set_b

# Proper subset operator:
# set_a < set_b


# ------------------------------------------------------------
# 1. What is a Subset?
# ------------------------------------------------------------

# Set A is a subset of Set B if:
# Every element of A exists in B.

# If A == B → still a subset.
# If A != B → A is a proper subset of B.

# Mental Model:
# "Is everything in A inside B?"


# ------------------------------------------------------------
# 2. Using issubset()
# ------------------------------------------------------------

numbers = {1, 2, 3, 4, 5}
scores = {1, 2, 3}

print(scores.issubset(numbers))  # True

# A set is always a subset of itself

print(numbers.issubset(numbers))  # True

# Not subset case

print(numbers.issubset(scores))  # False


# ------------------------------------------------------------
# 3. Using <= Operator (Subset)
# ------------------------------------------------------------

numbers = {1, 2, 3, 4, 5}
scores = {1, 2, 3}

print(scores <= numbers)  # True
print(numbers <= numbers)  # True

# Equivalent to issubset()


# ------------------------------------------------------------
# 4. Using < Operator (Proper Subset)
# ------------------------------------------------------------

numbers = {1, 2, 3, 4, 5}
scores = {1, 2, 3}

print(scores < numbers)  # True
print(numbers < numbers)  # False

# Proper subset means:
# - Must be subset
# - Must NOT be equal


# ------------------------------------------------------------
# 5. Important Rules
# ------------------------------------------------------------

# 1. <= checks subset (allows equality).
# 2. < checks proper subset (no equality).
# 3. A set is always a subset of itself.
# 4. Order does not matter (sets are unordered).


# ------------------------------------------------------------
# 6. Performance
# ------------------------------------------------------------

# Time Complexity:
# O(len(set_a)) average case

# Python checks:
# For each element in set_a,
# membership in set_b (O(1) average).


# ------------------------------------------------------------
# 7. Common Mistakes
# ------------------------------------------------------------

# Mistake 1: Confusing subset direction

a = {1, 2}
b = {1, 2, 3}

print(a <= b)  # True
print(b <= a)  # False


# Mistake 2: Thinking < behaves like <=

print(a < a)  # False
print(a <= a)  # True


# ------------------------------------------------------------
# 8. Key Insight
# ------------------------------------------------------------

# Subset is a containment check.

# Think:
# A <= B  →  "A fits inside B"

# Opposite concept:
# Superset (B >= A)
