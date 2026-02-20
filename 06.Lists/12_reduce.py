# ------------------------------------------------------------
# Python reduce() Function
# ------------------------------------------------------------

# reduce() → reduces a list to a single value
# syntax: reduce(function, iterable)

# NOTE: not built-in → import required
from functools import reduce

# ------------------------------------------------------------
# Basic Example (Sum)
# ------------------------------------------------------------

scores = [75, 65, 80, 95, 50]

total = reduce(lambda a, b: a + b, scores)
print(total)  # 365


# ------------------------------------------------------------
# How reduce() works internally
# ------------------------------------------------------------

# Step-by-step:
# (((75 + 65) + 80) + 95) + 50

# i.e.
# a=75, b=65 → 140
# a=140, b=80 → 220
# a=220, b=95 → 315
# a=315, b=50 → 365


# ------------------------------------------------------------
# With custom function (for clarity)
# ------------------------------------------------------------


def add(a, b):
    return a + b


scores = [75, 65, 80]
print(reduce(add, scores))  # 220


# ------------------------------------------------------------
# Other Use Cases
# ------------------------------------------------------------

# 1. Product of numbers
nums = [1, 2, 3, 4]
product = reduce(lambda a, b: a * b, nums)
print(product)  # 24

# 2. Find max
nums = [10, 50, 20, 5]
maximum = reduce(lambda a, b: a if a > b else b, nums)
print(maximum)  # 50


# ------------------------------------------------------------
# Important Insight
# ------------------------------------------------------------

# map()    → transforms each element
# filter() → selects some elements
# reduce() → combines all elements into ONE value


# ------------------------------------------------------------
# Initial Value (IMPORTANT)
# ------------------------------------------------------------

nums = [1, 2, 3]

# start from 10
result = reduce(lambda a, b: a + b, nums, 10)
print(result)  # 16  (10 + 1 + 2 + 3)


# ------------------------------------------------------------
# Pythonic Alternatives (VERY IMPORTANT)
# ------------------------------------------------------------

# Instead of reduce for sum:
nums = [1, 2, 3]
print(sum(nums))  # preferred

# Instead of reduce for max:
print(max(nums))  # preferred


# ------------------------------------------------------------
# Key Takeaway
# ------------------------------------------------------------

# reduce is powerful but:
# - less readable sometimes
# - often replaced by built-ins like sum(), max(), min()

# Use reduce when:
# → you need custom accumulation logic
