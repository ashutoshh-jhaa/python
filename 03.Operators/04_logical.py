# ------------------------------------------------------------
# Python Logical Operators
# ------------------------------------------------------------
# Logical operators are used to combine multiple conditions.
#
# Python has three logical operators:
# 1. and
# 2. or
# 3. not


# ------------------------------------------------------------
# 1. AND Operator
# ------------------------------------------------------------
# Returns True only if BOTH conditions are True.

price = 9.99

result = price > 9 and price < 10
print("price > 9 and price < 10:", result)

result = price > 10 and price < 20
print("price > 10 and price < 20:", result)


# Truth Table for AND
# True  and True  -> True
# True  and False -> False
# False and True  -> False
# False and False -> False


# ------------------------------------------------------------
# 2. OR Operator
# ------------------------------------------------------------
# Returns True if AT LEAST ONE condition is True.

result = price > 10 or price < 20
print("price > 10 or price < 20:", result)

result = price > 10 or price < 5
print("price > 10 or price < 5:", result)


# Truth Table for OR
# True  or True  -> True
# True  or False -> True
# False or True  -> True
# False or False -> False


# ------------------------------------------------------------
# 3. NOT Operator
# ------------------------------------------------------------
# Reverses the result of a condition.

result = not price > 10
print("not price > 10:", result)

result = not (price > 5 and price < 10)
print("not (price > 5 and price < 10):", result)


# Truth Table for NOT
# not True  -> False
# not False -> True


# ------------------------------------------------------------
# Operator Precedence
# ------------------------------------------------------------
# Logical operator precedence (highest to lowest):
# 1. not
# 2. and
# 3. or

a = True
b = False
c = True
d = False

print("a or b and c:", a or b and c)
# Equivalent to: a or (b and c)

print("a and b or c and d:", a and b or c and d)
# Equivalent to: (a and b) or (c and d)

print("not a and b or c:", not a and b or c)
# Equivalent to: ((not a) and b) or c


# ------------------------------------------------------------
# Important Python-Specific Insight
# ------------------------------------------------------------
# Logical operators in Python use short-circuit evaluation.
#
# For 'and':
# If the first condition is False,
# Python does NOT evaluate the second condition.
#
# For 'or':
# If the first condition is True,
# Python does NOT evaluate the second condition.


def check():
    print("Function executed")
    return True


print("Short-circuit AND example:")
False and check()  # check() will NOT run

print("Short-circuit OR example:")
True or check()  # check() will NOT run
