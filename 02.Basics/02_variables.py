# ------------------------------------------------------------
# Python Variables
# ------------------------------------------------------------
# In this section, we learn what variables are and how to use them.


# ------------------------------------------------------------
# What is a Variable?
# ------------------------------------------------------------
# When writing programs, we need to store and manage data.
# Variables are used to store values.
#
# In Python, a variable is simply a label that refers to a value.
# A variable is always associated with an object (value).


# Example:

message = "Hello, World!"
print(message)

message = "Good Bye!"
print(message)

# Explanation:
# - 'message' is a variable.
# - It first refers to the string 'Hello, World!'.
# - Later, it is reassigned to 'Good Bye!'.
# - A variable can refer to different values during program execution.
# - This is possible because Python is dynamically typed.


# ------------------------------------------------------------
# Creating Variables
# ------------------------------------------------------------
# Syntax:
# variable_name = value
#
# The '=' is called the assignment operator.
# It assigns the value on the right to the variable on the left.


# Example:

counter = 1

# Here:
# - 'counter' is the variable name.
# - 1 is the value assigned to it.


# ------------------------------------------------------------
# Naming Variables (Rules)
# ------------------------------------------------------------
# 1. Variable names can contain:
#    - Letters (a-z, A-Z)
#    - Numbers (0-9)
#    - Underscores (_)
#
# 2. They must start with:
#    - A letter
#    - Or an underscore (_)
#
#    They cannot start with a number.
#
# 3. Variable names cannot contain spaces.
#    Use underscores instead.
#    Example: sorted_list
#
# 4. Variable names cannot be:
#    - Python keywords
#    - Reserved words
#    - Built-in function names (like print, max, list, etc.)


# ------------------------------------------------------------
# Naming Variables (Best Practices)
# ------------------------------------------------------------
# - Use descriptive names.
#   Example:
#       active_user  (good)
#       au           (not descriptive)
#
# - Use underscores to separate words (snake_case style).
#
# - Avoid confusing characters:
#       lowercase l  (l)
#       uppercase O  (O)
#   Because they look like:
#       1 (one)
#       0 (zero)


# ------------------------------------------------------------
# Important Insight
# ------------------------------------------------------------
# In Python, variables do not store the actual value directly.
# Instead, they reference (point to) an object in memory.
#
# This is different from some lower-level languages.
#
# Example:
a = 10
b = a

# Both 'a' and 'b' now reference the same object (10).
