# ------------------------------------------------------------
# Lists: Unpacking
# ------------------------------------------------------------

# ------------------------------------------------------------
# 1. Basic Unpacking
# ------------------------------------------------------------

colors = ["red", "blue", "green"]

red, blue, green = colors

print(red)  # red
print(blue)  # blue
print(green)  # green


# ------------------------------------------------------------
# 2. Must match number of variables
# ------------------------------------------------------------

# colors = ['red', 'blue', 'green']
# red, blue = colors   # ❌ ERROR
# ValueError: too many values to unpack


# ------------------------------------------------------------
# 3. Using * (Packing remaining values)
# ------------------------------------------------------------

colors = ["red", "blue", "green"]

red, blue, *other = colors

print(red)  # red
print(blue)  # blue
print(other)  # ['green']


# ------------------------------------------------------------
# 4. More elements
# ------------------------------------------------------------

colors = ["cyan", "magenta", "yellow", "black"]

c, m, *rest = colors

print(c)  # cyan
print(m)  # magenta
print(rest)  # ['yellow', 'black']


# ------------------------------------------------------------
# 5. * can be in middle
# ------------------------------------------------------------

numbers = [1, 2, 3, 4, 5]

first, *middle, last = numbers

print(first)  # 1
print(middle)  # [2, 3, 4]
print(last)  # 5


# ------------------------------------------------------------
# 6. Ignore values using _
# ------------------------------------------------------------

a, _, c = [10, 20, 30]

print(a)  # 10
print(c)  # 30


# ------------------------------------------------------------
# 7. Swap variables (Very common)
# ------------------------------------------------------------

a = 10
b = 20

a, b = b, a

print(a, b)  # 20 10


# ------------------------------------------------------------
# 8. Works with tuples too
# ------------------------------------------------------------

point = (5, 10)

x, y = point

print(x, y)


# ------------------------------------------------------------
# 9. Important Insight
# ------------------------------------------------------------
# * always collects remaining values into a LIST

a, *b = (1, 2, 3)

print(type(b))  # <class 'list'>


# ------------------------------------------------------------
# Summary
# ------------------------------------------------------------
# - a, b = list → unpack
# - *rest → collects remaining elements
# - must match count unless using *
# - very useful for swapping & cleaner code
