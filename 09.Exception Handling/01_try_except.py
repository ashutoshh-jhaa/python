# ------------------------------------------------------------
# Python try...except (Exception Handling)
# ------------------------------------------------------------

# Basic syntax:
#
# try:
#     # risky code
# except SomeException:
#     # handle error


# ------------------------------------------------------------
# 1. Types of Errors
# ------------------------------------------------------------

# 1. SyntaxError → invalid Python code (caught before execution)
# 2. Exceptions → runtime errors (during execution)

# Example of SyntaxError:
#
# if x < 10
#     print(x)
#
# Missing colon → SyntaxError


# ------------------------------------------------------------
# 2. What is an Exception?
# ------------------------------------------------------------

# Runtime error.
# Examples:
# - ValueError
# - ZeroDivisionError
# - TypeError
# - NameError
# - FileNotFoundError


# ------------------------------------------------------------
# 3. Basic try...except
# ------------------------------------------------------------

try:
    x = int(input("Enter a number: "))
    print(10 / x)
except:
    print("Something went wrong.")

# Flow:
# 1. Try block runs.
# 2. If error occurs → jump to except.
# 3. Remaining try code is skipped.


# ------------------------------------------------------------
# 4. Catching Specific Exceptions
# ------------------------------------------------------------

try:
    previous = float(input("Prior: "))
    current = float(input("Current: "))

    change = (current - previous) * 100 / previous
    print(change)

except ValueError:
    print("Please enter valid numbers.")

except ZeroDivisionError:
    print("Previous value cannot be zero.")

# Important:
# Always catch specific exceptions when possible.


# ------------------------------------------------------------
# 5. Multiple Exceptions (Grouped)
# ------------------------------------------------------------

try:
    x = int(input("Enter number: "))
    print(10 / x)

except (ValueError, ZeroDivisionError):
    print("Invalid input or division by zero.")


# ------------------------------------------------------------
# 6. Catching Exception Object
# ------------------------------------------------------------

try:
    x = 10 / 0
except Exception as error:
    print("Error:", error)

# Exception is base class of most errors.
# Should be placed LAST.


# ------------------------------------------------------------
# 7. Execution Rules
# ------------------------------------------------------------

# 1. If no error → except skipped.
# 2. If error in try → jump to first matching except.
# 3. Only one except block executes.
# 4. After except → program continues normally.


# ------------------------------------------------------------
# 8. Common Mistakes
# ------------------------------------------------------------

# Mistake 1: Bare except (not recommended)

try:
    x = int("abc")
except:
    print("Bad practice.")

# Better:
# except ValueError:


# Mistake 2: Catching Exception first

# Wrong:
# except Exception:
# except ValueError:
#
# Specific exceptions must come before general Exception.


# ------------------------------------------------------------
# 9. Performance Note
# ------------------------------------------------------------

# try block itself has very small overhead.
# Raising exceptions is expensive.
# Do NOT use exceptions for normal control flow.


# ------------------------------------------------------------
# 10. Key Mental Model
# ------------------------------------------------------------

# try = attempt
# except = recovery

# Think:
# "If something breaks, how do I recover gracefully?"

# Goal:
# Prevent program crash.
# Provide user-friendly error messages.
