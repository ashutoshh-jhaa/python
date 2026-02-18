# ------------------------------------------------------------
# Python Constants
# ------------------------------------------------------------
# Summary:
# Python does not have true constant variables.
# Instead, constants are defined by naming convention.


# ------------------------------------------------------------
# What Are Constants?
# ------------------------------------------------------------
# In many programming languages (like C++ or Java),
# constants are variables whose values cannot be changed
# once assigned.
#
# Example in C++:
#     const int x = 10;
#
# Python does NOT have a built-in keyword like 'const'.


# ------------------------------------------------------------
# Defining Constants in Python (By Convention)
# ------------------------------------------------------------
# By convention, variables written in ALL CAPITAL LETTERS
# are treated as constants.

FILE_SIZE_LIMIT = 2000
print("FILE_SIZE_LIMIT:", FILE_SIZE_LIMIT)


# ------------------------------------------------------------
# Important: Python Does NOT Enforce Constants
# ------------------------------------------------------------
# You can still reassign the variable without error.

FILE_SIZE_LIMIT = 5000
print("Modified FILE_SIZE_LIMIT:", FILE_SIZE_LIMIT)

# Python allows this because:
# Variables in Python are just names bound to objects.
# There is no restriction preventing rebinding.


# ------------------------------------------------------------
# Why Python Doesn't Have True Constants
# ------------------------------------------------------------
# In Python:
#   - Variables are names.
#   - Names point to objects.
#   - Reassignment simply changes the binding.
#
# Example:

x = 10
print("x:", x)

x = 20  # This does not modify 10.
print("x after rebinding:", x)

# Python simply makes 'x' point to a new object.


# ------------------------------------------------------------
# Comparison with C++ (Conceptual Difference)
# ------------------------------------------------------------
# C++:
#   Variables represent memory locations.
#   'const' prevents modification of that memory.
#
# Python:
#   Names are references to objects.
#   There is no fixed memory slot to lock.
#
# Therefore, constants are not enforced at the language level.


# ------------------------------------------------------------
# Optional: Using typing.Final (Static Hint Only)
# ------------------------------------------------------------
# This helps static type checkers but does NOT
# prevent reassignment at runtime.

from typing import Final

MAX_USERS: Final = 100
print("MAX_USERS:", MAX_USERS)

# You can still reassign it at runtime (not recommended)
MAX_USERS = 200
print("Modified MAX_USERS:", MAX_USERS)
