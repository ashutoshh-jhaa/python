# ------------------------------------------------------------
# Python List: Finding Index
# ------------------------------------------------------------

cities = ["New York", "Beijing", "Cairo", "Mumbai", "Mexico"]

# Basic usage
index = cities.index("Mumbai")
print(index)  # 3


# ------------------------------------------------------------
# Important Behavior
# ------------------------------------------------------------

# 1. Returns FIRST occurrence only
numbers = [1, 2, 3, 2, 4]
print(numbers.index(2))  # 1 (not 3)


# 2. Raises error if element not found
# cities.index('Osaka')  # ValueError


# ------------------------------------------------------------
# Safe Approach
# ------------------------------------------------------------

city = "Osaka"

if city in cities:
    print(cities.index(city))
else:
    print("Not found")


# ------------------------------------------------------------
# Advanced Insight
# ------------------------------------------------------------

# index() is O(n) → linear search
# Avoid repeated calls in loops (inefficient)

# BAD as O(n)*O(n) = O(n^2)
for city in cities:  # O(n)
    print(cities.index(city))  # slow (nested search) O(n)

# GOOD
for i, city in enumerate(cities):
    print(i, city)


# ------------------------------------------------------------
# Pro Tip
# ------------------------------------------------------------

# If you need index frequently → use enumerate()
# If you need search once → use index()
