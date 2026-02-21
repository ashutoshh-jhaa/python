# ------------------------------------------------------------
# Python List Comprehensions
# ------------------------------------------------------------

# Basic syntax:
# [expression for item in iterable]

# Equivalent to:
# result = []
# for item in iterable:
#     result.append(expression)


# ------------------------------------------------------------
# 1. Basic Transformation
# ------------------------------------------------------------

numbers = [1, 2, 3, 4, 5]

# Create squares
squares = [number**2 for number in numbers]

print(squares)  # [1, 4, 9, 16, 25]


# ------------------------------------------------------------
# 2. With Condition (Filtering)
# ------------------------------------------------------------

numbers = [1, 2, 3, 4, 5, 6]

# Only even numbers
evens = [n for n in numbers if n % 2 == 0]

print(evens)  # [2, 4, 6]


# ------------------------------------------------------------
# 3. Transformation + Condition
# ------------------------------------------------------------

numbers = [1, 2, 3, 4, 5, 6]

# Square only even numbers
result = [n**2 for n in numbers if n % 2 == 0]

print(result)  # [4, 16, 36]


# ------------------------------------------------------------
# 4. With Complex Data
# ------------------------------------------------------------

mountains = [["Makalu", 8485], ["Lhotse", 8516], ["K2", 8611], ["Everest", 8848]]

# Filter mountains > 8600m
highest = [m for m in mountains if m[1] > 8600]

print(highest)


# ------------------------------------------------------------
# 5. If-Else (Ternary inside comprehension)
# ------------------------------------------------------------

numbers = [1, 2, 3, 4]

labels = ["even" if n % 2 == 0 else "odd" for n in numbers]

print(labels)  # ['odd', 'even', 'odd', 'even']


# ------------------------------------------------------------
# 6. Equivalent using map + filter
# ------------------------------------------------------------

# map:
squares = list(map(lambda n: n**2, numbers))

# filter:
evens = list(filter(lambda n: n % 2 == 0, numbers))

# List comprehension replaces BOTH:
combined = [n**2 for n in numbers if n % 2 == 0]
