# ------------------------------------------------------------
# Python map() Function
# ------------------------------------------------------------

# ------------------------------------------------------------
# 1. What map() does
# ------------------------------------------------------------
# Applies a function to every element of an iterable

# Syntax:
# map(function, iterable)


# ------------------------------------------------------------
# 2. Basic Example
# ------------------------------------------------------------

numbers = [1, 2, 3]

result = map(lambda x: x * 2, numbers)

print(list(result))  # [2, 4, 6]


# ------------------------------------------------------------
# 3. Equivalent using loop
# ------------------------------------------------------------

numbers = [1, 2, 3]
new = []

for n in numbers:
    new.append(n * 2)

print(new)


# ------------------------------------------------------------
# 4. Important: map() returns an iterator
# ------------------------------------------------------------

numbers = [1, 2, 3]
m = map(lambda x: x * 2, numbers)

print(m)  # <map object ...>
print(list(m))  # [2, 4, 6]
print(list(m))  # []  (already consumed)


# ------------------------------------------------------------
# 5. With normal function
# ------------------------------------------------------------


def square(x):
    return x * x


nums = [1, 2, 3]
print(list(map(square, nums)))  # [1, 4, 9]


# ------------------------------------------------------------
# 6. With strings
# ------------------------------------------------------------

names = ["ash", "rahul"]
print(list(map(str.upper, names)))  # ['ASH', 'RAHUL']


# ------------------------------------------------------------
# 7. With multiple iterables (IMPORTANT)
# ------------------------------------------------------------

a = [1, 2, 3]
b = [4, 5, 6]

result = map(lambda x, y: x + y, a, b)
print(list(result))  # [5, 7, 9]


# ------------------------------------------------------------
# Summary
# ------------------------------------------------------------
# map() → applies function to each element
# returns → iterator (lazy)
# often used with lambda
