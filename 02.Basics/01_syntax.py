# Python uses whitespace (indentation) to define code blocks.
# Indentation is mandatory and replaces curly braces used in languages like C++ or Java.
# The standard indentation level is 4 spaces.

# Example: Code Structure
def main():
    i = 1
    max_value = 10  # Avoid using built-in names like 'max'

    while i < max_value:
        print(i)
        i = i + 1


# Call the function
main()


# ------------------------------------------------------------
# Comments in Python
# ------------------------------------------------------------

# This is a single-line comment.

# Python does not have a dedicated multi-line comment syntax.
# However, triple-quoted strings are often used for documentation.

"""
This is a multi-line string.
It is commonly used as a docstring for documentation.
"""


# ------------------------------------------------------------
# Statements and Line Continuation
# ------------------------------------------------------------

# Python typically places one statement per line.

# A long statement can be split across multiple lines using
# the backslash (\) character for explicit continuation.

# Example:
# if (a == True) and (b == False) and \
#    (c == True):
#     print("Continuation of statement")

# A better and cleaner approach is to use parentheses,
# which allow implicit line continuation.

# Example:
# if (
#     a == True
#     and b == False
#     and c == True
# ):
#     print("Cleaner continuation")


# ------------------------------------------------------------
# Identifiers
# ------------------------------------------------------------

# Identifiers are names given to variables, functions, classes, etc.
# Rules:
# - Identifiers are case-sensitive.
# - They can contain letters, digits, and underscores.
# - They cannot start with a digit.
# - They cannot be Python keywords.


# ------------------------------------------------------------
# Keywords
# ------------------------------------------------------------

# Keywords are reserved words in Python.
# They cannot be used as identifiers.

# Python provides a built-in module called 'keyword'
# to list all current keywords.

# Example:
# import keyword
# print(keyword.kwlist)

# The list of keywords may change between Python versions.


# ------------------------------------------------------------
# String Literals
# ------------------------------------------------------------

# Python supports three types of string literals:

# 1. Single quotes
#    'Hello'

# 2. Double quotes
#    "Hello"

# 3. Triple quotes (single or double)
#    Used for multi-line strings or documentation

#    """
#    This is a multi-line string.
#    """
