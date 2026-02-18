# ------------------------------------------------------------
# Python Comments
# ------------------------------------------------------------
# Summary:
# Comments are used to explain code.
# The Python interpreter ignores comments during execution.


# ------------------------------------------------------------
# 1. Block Comments
# ------------------------------------------------------------
# A block comment explains the code that follows it.
# It usually appears above the related code.

price = 100

# Increase price by 5%
price = price * 1.05
print("Updated price:", price)


# ------------------------------------------------------------
# 2. Inline Comments
# ------------------------------------------------------------
# Inline comments appear on the same line as code.

salary = 120000
salary = salary * 1.02  # Increase salary by 2%

print("Updated salary:", salary)


# ------------------------------------------------------------
# 3. Docstrings (Documentation Strings)
# ------------------------------------------------------------
# Docstrings are string literals placed as the first line
# inside a module, function, or class.
#
# Unlike regular comments:
# - They are NOT ignored by Python.
# - They can be accessed at runtime using __doc__.
#
# They are mainly used for documentation.


# ------------------------------------------------------------
# One-line Docstring
# ------------------------------------------------------------


def greet():
    """Return a greeting message."""
    return "Hello"


print(greet())
print("Docstring of greet():", greet.__doc__)


# ------------------------------------------------------------
# Multi-line Docstring
# ------------------------------------------------------------


def increase_salary(salary, percentage, rating):
    """
    Increase salary based on rating and percentage.

    rating 1 - 2 : no increase
    rating 3 - 4 : increase 5%
    rating 5 - 6 : increase 10%
    """
    if rating <= 2:
        return salary
    elif rating <= 4:
        return salary * 1.05
    else:
        return salary * 1.10


print("New salary:", increase_salary(100000, 5, 5))
print("Docstring of increase_salary():")
print(increase_salary.__doc__)


# ------------------------------------------------------------
# Multiline Comments in Python
# ------------------------------------------------------------
# Python does NOT have true multiline comments.
#
# However, developers often use triple-quoted strings
# as temporary multiline comments.

"""
This is a multi-line string.
It can act like a multiline comment.
But technically, it is just a string literal.
"""


# ------------------------------------------------------------
# Important Notes
# ------------------------------------------------------------
# - Block and inline comments start with '#'.
# - Docstrings use triple quotes.
# - Docstrings are accessible at runtime.
# - Good comments should be clear and concise.
