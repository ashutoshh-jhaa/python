# ------------------------------------------------------------
# Control Flow: pass Statement
# ------------------------------------------------------------
# The pass statement does nothing.
# It is used as a placeholder where a statement is required.


# ------------------------------------------------------------
# 1. Basic Usage
# ------------------------------------------------------------

if True:
    pass  # Placeholder (no action)


# ------------------------------------------------------------
# 2. Why pass is Needed
# ------------------------------------------------------------
# Python requires a block after statements like if, for, while, etc.

# This would cause an error:
# if True:
#     # nothing here → SyntaxError

# Correct way:
if True:
    pass


# ------------------------------------------------------------
# 3. Using pass in Loops
# ------------------------------------------------------------

for i in range(5):
    pass  # Loop runs but does nothing

counter = 0
while counter < 3:
    counter += 1
    pass  # Again, nothing happens


# ------------------------------------------------------------
# 4. Using pass in Functions and Classes
# ------------------------------------------------------------


def my_function():
    pass  # To be implemented later


class MyClass:
    pass  # Empty class


# ------------------------------------------------------------
# 5. Important: while True + pass
# ------------------------------------------------------------

# WARNING: This creates an infinite busy loop

# while True:
#     pass

# Behavior:
# - Runs forever
# - Does nothing
# - Consumes CPU heavily
# - Can freeze your system

# Safe version (adds delay):
# import time
# while True:
#     print("Running...")
#     time.sleep(1)


# ------------------------------------------------------------
# 6. pass vs continue
# ------------------------------------------------------------
# pass     → does nothing
# continue → skips current iteration

for i in range(5):
    if i == 2:
        pass  # does nothing
    print("pass example:", i)

for i in range(5):
    if i == 2:
        continue  # skips this iteration
    print("continue example:", i)


# ------------------------------------------------------------
# Summary
# ------------------------------------------------------------
# - pass is a placeholder statement
# - It does nothing but avoids syntax errors
# - Useful during development
# - Avoid using pass in infinite loops without control
