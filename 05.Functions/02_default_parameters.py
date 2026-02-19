# ------------------------------------------------------------
# Functions: Default Parameters
# ------------------------------------------------------------
# Default parameters allow you to assign a default value
# to function parameters.


# ------------------------------------------------------------
# 1. Basic Example
# ------------------------------------------------------------


def greet(name, message="Hi"):
    return f"{message} {name}"


print(greet("John", "Hello"))  # Hello John
print(greet("John"))  # Hi John (default used)


# ------------------------------------------------------------
# 2. Multiple Default Parameters
# ------------------------------------------------------------


def greet_all(name="there", message="Hi"):
    return f"{message} {name}"


print(greet_all())  # Hi there


# ------------------------------------------------------------
# 3. Important Behavior (Positional Arguments)
# ------------------------------------------------------------

print(greet_all("Hello"))
# Output: Hi Hello
# Explanation:
# 'Hello' is assigned to 'name', NOT 'message'


# ------------------------------------------------------------
# 4. Using Keyword Arguments
# ------------------------------------------------------------

print(greet_all(message="Hello"))
# Output: Hello there


# ------------------------------------------------------------
# Important Rule (Very Important)
# ------------------------------------------------------------
# Once a parameter has a default value,
# all parameters to the right must also have default values.

# ------------------------------------------------------------
# Why This Rule Exists
# ------------------------------------------------------------
# Python assigns arguments from left to right.
# Mixing default and non-default parameters incorrectly
# creates ambiguity.


# ------------------------------------------------------------
# Comparison with C++
# ------------------------------------------------------------
# Same rule exists in C++:
# once default starts → all parameters after must have defaults
#
# Python advantage:
# supports keyword arguments to skip parameters


# ------------------------------------------------------------
# Summary
# ------------------------------------------------------------
# - Default parameters simplify function calls
# - Arguments are assigned positionally by default
# - Use keyword arguments for flexibility
# - Follow parameter ordering rules
