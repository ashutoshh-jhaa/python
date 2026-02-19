# ------------------------------------------------------------
# Control Flow: Python Ternary Operator
# ------------------------------------------------------------
# The ternary operator provides a shorter way to write
# simple if...else assignments.


# ------------------------------------------------------------
# 1. Standard if...else Version
# ------------------------------------------------------------

age = 19

if age >= 18:
    ticket_price = 20
else:
    ticket_price = 5

print("Using if...else:", ticket_price)


# ------------------------------------------------------------
# 2. Ternary Operator Version
# ------------------------------------------------------------
# Syntax:
# value_if_true if condition else value_if_false

ticket_price = 20 if age >= 18 else 5
print("Using ternary operator:", ticket_price)


# ------------------------------------------------------------
# How It Works
# ------------------------------------------------------------
# The expression:
#
# 20 if age >= 18 else 5
#
# Means:
# - If age >= 18 is True → return 20
# - Otherwise → return 5


# ------------------------------------------------------------
# Example with Type Conversion
# ------------------------------------------------------------

age = "20"

ticket_price = 20 if int(age) >= 18 else 5
print(f"The ticket price is ${ticket_price}")


# ------------------------------------------------------------
# Important Notes
# ------------------------------------------------------------
# 1. Ternary operator is used for simple decisions.
# 2. Avoid complex nested ternary expressions.
# 3. It improves readability only when kept simple.
#
# Python does NOT support C/Java style:
# condition ? value_if_true : value_if_false
#
# Python uses:
# value_if_true if condition else value_if_false
