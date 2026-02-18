# ------------------------------------------------------------
# Python Numbers
# ------------------------------------------------------------
# Python supports three numeric types:
# 1. int      -> integers
# 2. float    -> floating-point numbers
# 3. complex  -> complex numbers (not covered here)


# ------------------------------------------------------------
# Integers (int)
# ------------------------------------------------------------
# Integers are whole numbers:
# -1, 0, 1, 2, 3, ...

x = 20
y = 10

# Basic arithmetic operations
total = x + y
print("Addition:", total)

difference = x - y
print("Subtraction:", difference)

product = x * y
print("Multiplication:", product)

quotient = x / y  # Division always returns float
print("Division:", quotient)


# ------------------------------------------------------------
# Exponentiation
# ------------------------------------------------------------
# Use ** for powers

x = 3
y = 3

power = x**y
print("Power:", power)


# ------------------------------------------------------------
# Order of Operations
# ------------------------------------------------------------
# Use parentheses to control precedence

result = 20 / (10 + 10)
print("With parentheses:", result)


# ------------------------------------------------------------
# Floats (float)
# ------------------------------------------------------------
# Any number with a decimal point is a float

x = 0.5
y = 0.25

print("Float addition:", x + y)
print("Float subtraction:", x - y)
print("Float multiplication:", x * y)
print("Float division:", x / y)


# ------------------------------------------------------------
# Division Behavior
# ------------------------------------------------------------
# Division of two integers returns a float

x = 20
y = 10
print("Integer division result:", x / y)  # 2.0


# ------------------------------------------------------------
# Mixing int and float
# ------------------------------------------------------------
# Result becomes float

x = 1
y = 2.0

print("Mixed result:", x + y)


# ------------------------------------------------------------
# Floating-Point Precision Issue
# ------------------------------------------------------------
# Due to internal binary representation of floats,
# some results may look unexpected.

x = 0.1
y = 0.2
total = x + y

print("0.1 + 0.2 =", total)

# Expected: 0.3
# Actual:   0.30000000000000004
#
# This happens because decimal fractions cannot always
# be represented exactly in binary.


# ------------------------------------------------------------
# Underscores in Numbers (Python 3.6+)
# ------------------------------------------------------------
# Underscores improve readability in large numbers.

count = 10_000_000_000
print("Large number:", count)

# Python ignores underscores internally.
# Works for both integers and floats.

large_float = 1_000_000.50
print("Large float:", large_float)


# ------------------------------------------------------------
# Useful Additional Operators (Important)
# ------------------------------------------------------------

# Floor division (removes decimal part)
print("Floor division:", 7 // 2)  # 3

# Modulus (remainder)
print("Modulus:", 7 % 2)  # 1
