# ------------------------------------------------------------
# Python Set Difference
# ------------------------------------------------------------

# Basic syntax (method):
# set1.difference(iterable1, iterable2, ...)

# Basic syntax (operator):
# set1 - set2


# ------------------------------------------------------------
# 1. Difference of Two Sets
# ------------------------------------------------------------

s1 = {"Python", "Java", "C++"}
s2 = {"C#", "Java", "C++"}

result = s1.difference(s2)

print(result)  # {'Python'}

# Mental Model:
# Keep elements from FIRST set
# Remove anything that appears in SECOND set

# Time Complexity:
# O(len(s1)) average case


# ------------------------------------------------------------
# 2. Difference is NOT Commutative
# ------------------------------------------------------------

s1 = {"Python", "Java", "C++"}
s2 = {"C#", "Java", "C++"}

print(s1 - s2)  # {'Python'}
print(s2 - s1)  # {'C#'}

# Order matters:
# A - B != B - A


# ------------------------------------------------------------
# 3. Using - Operator
# ------------------------------------------------------------

s1 = {"Python", "Java", "C++"}
s2 = {"C#", "Java", "C++"}

result = s1 - s2
print(result)


# ------------------------------------------------------------
# 4. Multiple Set Difference
# ------------------------------------------------------------

a = {1, 2, 3, 4}
b = {2}
c = {3}

result = a.difference(b, c)
print(result)  # {1, 4}

# Equivalent:
result = a - b - c
print(result)


# ------------------------------------------------------------
# 5. difference() Accepts Any Iterable
# ------------------------------------------------------------

scores = {7, 8, 9}
numbers = [9, 10]

new_scores = scores.difference(numbers)

print(new_scores)  # {7, 8}

# Internally converts iterable → set


# ------------------------------------------------------------
# 6. - Operator Restriction
# ------------------------------------------------------------

scores = {7, 8, 9}
numbers = [9, 10]

# new_scores = scores - numbers
# TypeError: unsupported operand type(s) for -: 'set' and 'list'

# Fix:
new_scores = scores - set(numbers)


# ------------------------------------------------------------
# 7. Important Rules
# ------------------------------------------------------------

# 1. Returns a NEW set.
# 2. Original sets remain unchanged.
# 3. Order is not guaranteed.
# 4. Operation depends on left-hand operand.


# ------------------------------------------------------------
# 8. Common Mistakes
# ------------------------------------------------------------

# Mistake 1: Forgetting order matters

a = {1, 2, 3}
b = {2}

print(a - b)  # {1, 3}
print(b - a)  # set()


# Mistake 2: Expecting original set to change

a = {1, 2, 3}
b = {2}

a.difference(b)
print(a)  # still {1, 2, 3}

# Correct:
a = a.difference(b)


# ------------------------------------------------------------
# 9. Key Insight
# ------------------------------------------------------------

# Difference is a filtering operation:
# "Remove everything that exists in the other set."

# Think:
# A - B = elements unique to A

# Useful for:
# - Removing banned items
# - Finding missing values
# - Permission subtraction
