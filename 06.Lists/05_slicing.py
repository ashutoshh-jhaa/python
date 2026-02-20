# ------------------------------------------------------------
# Lists: Slicing
# ------------------------------------------------------------
# Syntax: list[start:end:step]
# - start → inclusive
# - end → exclusive
# - step → jump


# ------------------------------------------------------------
# 1. Basic Slicing
# ------------------------------------------------------------

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

print(colors[1:4])  # ['orange', 'yellow', 'green']


# ------------------------------------------------------------
# 2. Default Values
# ------------------------------------------------------------

print(colors[:3])  # first 3 elements
print(colors[3:])  # from index 3 to end
print(colors[:])  # full copy


# ------------------------------------------------------------
# 3. Negative Indexing
# ------------------------------------------------------------

print(colors[-3:])  # last 3 elements


# ------------------------------------------------------------
# 4. Step
# ------------------------------------------------------------

print(colors[::2])  # every 2nd element


# ------------------------------------------------------------
# 5. Reverse (Very Important)
# ------------------------------------------------------------

print(colors[::-1])  # reversed list


# ------------------------------------------------------------
# 6. Modifying using Slicing
# ------------------------------------------------------------

colors = ["red", "orange", "yellow", "green"]

colors[0:2] = ["black", "white"]
print(colors)


# ------------------------------------------------------------
# 7. Resizing List (Insert via slice)
# ------------------------------------------------------------

colors = ["red", "orange", "yellow"]

colors[0:2] = ["black", "white", "gray"]
print(colors)


# ------------------------------------------------------------
# 8. Deleting using Slicing
# ------------------------------------------------------------

colors = ["red", "orange", "yellow", "green", "blue"]

del colors[1:4]
print(colors)


# ------------------------------------------------------------
# 9. Important Insight (VERY IMPORTANT)
# ------------------------------------------------------------
# Slicing creates a NEW list (copy)

a = [1, 2, 3]
b = a[:]  # copy

b[0] = 100

print(a)  # [1, 2, 3]
print(b)  # [100, 2, 3]


# ------------------------------------------------------------
# 10. But beware (shallow copy)
# ------------------------------------------------------------

a = [[1], [2], [3]]
b = a[:]

b[0][0] = 100

print(a)  # [[100], [2], [3]]
print(b)


# Why?
# - outer list copied
# - inner lists still referenced


# ------------------------------------------------------------
# Summary
# ------------------------------------------------------------
# - list[start:end:step]
# - end is excluded
# - slicing creates new list
# - can modify, delete, resize using slicing
