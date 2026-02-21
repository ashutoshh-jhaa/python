# ------------------------------------------------------------
# Functions: Docstrings
# ------------------------------------------------------------
# Docstring = documentation string for functions, classes, modules


# ------------------------------------------------------------
# 1. Basic Docstring
# ------------------------------------------------------------


def add(a, b):
    "Return the sum of two arguments"
    return a + b


print(add(2, 3))


# ------------------------------------------------------------
# 2. Using help()
# ------------------------------------------------------------
# help() reads the docstring

help(add)


# ------------------------------------------------------------
# 3. Multi-line Docstring (Recommended)
# ------------------------------------------------------------


def multiply(a, b):
    """
    Multiply two numbers.

    Parameters:
        a (int/float): first number
        b (int/float): second number

    Returns:
        int/float: product of a and b
    """
    return a * b


help(multiply)


# ------------------------------------------------------------
# 4. Accessing Docstring Manually
# ------------------------------------------------------------

print(multiply.__doc__)


# ------------------------------------------------------------
# 5. Important Notes
# ------------------------------------------------------------
# - Docstring must be the FIRST statement in function
# - Uses triple quotes """ """
# - Not ignored like comments → stored in memory
# - Used by tools, IDEs, documentation generators


# ------------------------------------------------------------
# 6. Docstring vs Comment
# ------------------------------------------------------------
# Comment:
#   - ignored by Python
#   - for developers only
#
# Docstring:
#   - accessible at runtime
#   - used for documentation (help(), __doc__)


# ------------------------------------------------------------
# Summary
# ------------------------------------------------------------
# - Use docstrings to describe what function does
# - help() displays docstrings
# - stored in __doc__
