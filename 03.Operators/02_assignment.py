# ------------------------------------------------------------
# Python Assignment Operators
# ------------------------------------------------------------
# Assignment operators are used to assign values to variables.


# ------------------------------------------------------------
# 1. Basic Assignment (=)
# ------------------------------------------------------------

count = 0
print("Initial count:", count)

# Reassigning after calculation
count = count + 1
print("After increment:", count)

# Important:
# '=' is assignment, not comparison.
# '==' is used for comparison.


# ------------------------------------------------------------
# 2. Compound Assignment Operators
# ------------------------------------------------------------
# Compound operators combine an operation and assignment.


# += (Add and Assign)
count = 0
count += 1  # Same as: count = count + 1
print("+= result:", count)


# -= (Subtract and Assign)
quantity = 5
quantity -= 2  # Same as: quantity = quantity - 2
print("-= result:", quantity)


# *= (Multiply and Assign)
a = 10
a *= 2  # Same as: a = a * 2
print("*= result:", a)


# /= (Divide and Assign)
amount = 25
amount /= 2  # Same as: amount = amount / 2
print("/= result:", amount)


# //= (Floor Divide and Assign)
amount = 10
amount //= 3  # Same as: amount = amount // 3
print("//= result:", amount)


# %= (Modulus and Assign)
amount = 10
amount %= 3  # Same as: amount = amount % 3
print("%= result:", amount)


# **= (Exponentiate and Assign)
a = 2
a **= 3  # Same as: a = a ** 3
print("**= result:", a)
