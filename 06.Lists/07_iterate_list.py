# ------------------------------------------------------------
# Lists: Iteration using for loop
# ------------------------------------------------------------

# ------------------------------------------------------------
# 1. Basic iteration
# ------------------------------------------------------------

cities = ["New York", "Beijing", "Cairo", "Mumbai", "Mexico"]

for city in cities:
    print(city)


# ------------------------------------------------------------
# 2. Accessing index using enumerate()
# ------------------------------------------------------------

cities = ["New York", "Beijing", "Cairo"]

for index, city in enumerate(cities):
    print(index, city)

# 0 New York
# 1 Beijing
# 2 Cairo


# ------------------------------------------------------------
# 3. Custom start index
# ------------------------------------------------------------

for index, city in enumerate(cities, start=1):
    print(index, city)

# 1 New York
# 2 Beijing
# 3 Cairo


# ------------------------------------------------------------
# 4. enumerate returns tuples
# ------------------------------------------------------------

for item in enumerate(cities):
    print(item)

# (0, 'New York')
# (1, 'Beijing')
# (2, 'Cairo')


# ------------------------------------------------------------
# 5. When to use what
# ------------------------------------------------------------

# Only value → normal loop
for city in cities:
    pass

# Need index + value → use enumerate
for i, city in enumerate(cities):
    pass


# ------------------------------------------------------------
# 6. Modifying list while iterating (Important)
# ------------------------------------------------------------

numbers = [1, 2, 3, 4]

# BAD (can cause bugs)
for n in numbers:
    if n == 2:
        numbers.remove(n)

# SAFE approach
numbers = [1, 2, 3, 4]

for i in range(len(numbers)):
    if numbers[i] == 2:
        numbers[i] = 0


# ------------------------------------------------------------
# 7. Iterating using index (C/C++ style)
# ------------------------------------------------------------

for i in range(len(cities)):
    print(i, cities[i])


# ------------------------------------------------------------
# 8. Reverse iteration
# ------------------------------------------------------------

for city in reversed(cities):
    print(city)


# ------------------------------------------------------------
# Summary
# ------------------------------------------------------------
# - for item in list → simple iteration
# - enumerate() → index + value
# - avoid modifying list directly in loop
# - range(len()) → when index needed explicitly
