# ------------------------------------------------------------
# Control Flow: if Statements
# ------------------------------------------------------------
# Control flow allows a program to make decisions
# and execute code conditionally.


# ------------------------------------------------------------
# 1. Simple if Statement
# ------------------------------------------------------------
# Syntax:
# if condition:
#     block_of_code

age = 18

if age >= 18:
    print("You're eligible to vote.")


# ------------------------------------------------------------
# Important:
# - The colon (:) is mandatory.
# - Indentation defines the block.
# - Standard indentation: 4 spaces.
# ------------------------------------------------------------


# ------------------------------------------------------------
# 2. if with Multiple Statements
# ------------------------------------------------------------

age = 20

if age >= 18:
    print("You're eligible to vote.")
    print("Let's go and vote.")


# ------------------------------------------------------------
# Indentation Matters
# ------------------------------------------------------------

age = 11

if age >= 18:
    print("You're eligible to vote.")

print("This line runs regardless of the condition.")


# ------------------------------------------------------------
# 3. if...else Statement
# ------------------------------------------------------------

age = 15

if age >= 18:
    print("You're eligible to vote.")
else:
    print("You're not eligible to vote.")


# ------------------------------------------------------------
# 4. if...elif...else Statement
# ------------------------------------------------------------
# Used when checking multiple conditions.

age = 10

if age < 5:
    ticket_price = 5
elif age < 16:
    ticket_price = 10
else:
    ticket_price = 18

print(f"Ticket price: ${ticket_price}")


# ------------------------------------------------------------
# How Python Evaluates if...elif...else
# ------------------------------------------------------------
# 1. Checks conditions from top to bottom.
# 2. Executes the first True condition.
# 3. Skips the rest.
# 4. If none are True, runs else (if present).


# ------------------------------------------------------------
# Important Concept
# ------------------------------------------------------------
# Conditions must evaluate to True or False.
# Python uses truthy and falsy values.

value = ""

if value:
    print("Value is truthy.")
else:
    print("Value is falsy.")
