# ------------------------------------------------------------
# Python Comparison Operators
# ------------------------------------------------------------
# Comparison operators compare two values
# and return True or False.


# ------------------------------------------------------------
# 1. Less Than (<)
# ------------------------------------------------------------

print("10 < 20:", 10 < 20)
print("20 < 10:", 20 < 10)

# String comparison (lexicographical / dictionary order)
print("'apple' < 'orange':", "apple" < "orange")
print("'banana' < 'apple':", "banana" < "apple")


# ------------------------------------------------------------
# 2. Less Than or Equal (<=)
# ------------------------------------------------------------

print("20 <= 20:", 20 <= 20)
print("10 <= 20:", 10 <= 20)
print("30 <= 10:", 30 <= 10)


# ------------------------------------------------------------
# 3. Greater Than (>)
# ------------------------------------------------------------

print("20 > 10:", 20 > 10)
print("20 > 20:", 20 > 20)
print("10 > 20:", 10 > 20)

print("'orange' > 'apple':", "orange" > "apple")


# ------------------------------------------------------------
# 4. Greater Than or Equal (>=)
# ------------------------------------------------------------

print("20 >= 10:", 20 >= 10)
print("20 >= 20:", 20 >= 20)
print("10 >= 20:", 10 >= 20)

print("'apple' >= 'apple':", "apple" >= "apple")


# ------------------------------------------------------------
# 5. Equal To (==)
# ------------------------------------------------------------

print("20 == 10:", 20 == 10)
print("20 == 20:", 20 == 20)

print("'apple' == 'apple':", "apple" == "apple")


# ------------------------------------------------------------
# 6. Not Equal To (!=)
# ------------------------------------------------------------

print("20 != 20:", 20 != 20)
print("20 != 10:", 20 != 10)

print("'apple' != 'orange':", "apple" != "orange")


# ------------------------------------------------------------
# Important Python-Specific Insights
# ------------------------------------------------------------

# 1. == compares values
# 2. is compares object identity (memory reference)

a = 1000
b = 1000

print("a == b:", a == b)
print("a is b:", a is b)  # Often False for large integers

# Small integer caching (CPython Optimization)
# CPython automatically pre-creates and reuses integer objects
# in the range -5 to 256.
# This means numbers within this range may point to the same
# memory object.

x = 10
y = 10

print("x is y:", x is y)  # Often True
print("x == y:", x == y)

# Important:
# This behavior is an implementation detail of CPython.
# It is done for performance and memory optimization.
#
# You should NOT rely on this behavior in your logic.
# Always use '==' for value comparison.

# ------------------------------------------------------------
# Chained Comparisons (Python Feature)
# ------------------------------------------------------------

num = 15
print("10 < num < 20:", 10 < num < 20)

# Equivalent to:
# (10 < num) and (num < 20)
