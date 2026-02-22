# ------------------------------------------------------------
# Python try...except...finally
# ------------------------------------------------------------

# Basic syntax:
#
# try:
#     risky code
# except SomeException:
#     handle error
# finally:
#     cleanup code


# ------------------------------------------------------------
# 1. Purpose of finally
# ------------------------------------------------------------

# finally block ALWAYS executes:
# - Whether exception occurs or not
# - After try and except blocks

# Mental Model:
# try      → attempt
# except   → recover
# finally  → cleanup


# ------------------------------------------------------------
# 2. Example: Exception Occurs
# ------------------------------------------------------------

a = 10
b = 0

try:
    c = a / b
    print(c)
except ZeroDivisionError as error:
    print(error)
finally:
    print("Finishing up.")

# Output:
# division by zero
# Finishing up.


# ------------------------------------------------------------
# 3. Example: No Exception
# ------------------------------------------------------------

a = 10
b = 2

try:
    c = a / b
    print(c)
except ZeroDivisionError:
    print("Error occurred.")
finally:
    print("Finishing up.")

# Output:
# 5.0
# Finishing up.


# ------------------------------------------------------------
# 4. try...finally (Without except)
# ------------------------------------------------------------

# except is optional

try:
    print("Doing something risky.")
finally:
    print("Always executed.")

# Use case:
# When you cannot handle the error
# but still need to release resources.


# ------------------------------------------------------------
# 5. Real-World Use Case (Resource Cleanup)
# ------------------------------------------------------------

file = None

try:
    file = open("data.txt", "r")
    data = file.read()
    print(data)
finally:
    if file:
        file.close()
        print("File closed.")

# Ensures file closes even if error happens.


# ------------------------------------------------------------
# 6. Execution Order Rules
# ------------------------------------------------------------

# Case 1: No exception
# try → finally

# Case 2: Exception handled
# try → except → finally

# Case 3: Exception not handled
# try → finally → program crashes


# ------------------------------------------------------------
# 7. Important Behavior
# ------------------------------------------------------------

# finally executes even if:
# - return statement is inside try
# - break/continue inside try
# - exception occurs


def test():
    try:
        return 10
    finally:
        print("finally runs before returning")


print(test())


# ------------------------------------------------------------
# 8. Performance Note
# ------------------------------------------------------------

# try/finally has minimal overhead.
# Recommended for:
# - File handling
# - Database connections
# - Network sockets
# - Lock release


# ------------------------------------------------------------
# 9. Key Insight
# ------------------------------------------------------------

# finally is about guaranteed execution.

# Think:
# "No matter what happens,
# this code MUST run."
