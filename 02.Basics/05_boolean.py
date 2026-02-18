# ------------------------------------------------------------
# Python Boolean (bool)
# ------------------------------------------------------------
# The boolean data type represents logical values:
# True and False
#
# Note:
# - True and False must start with capital letters.
# - The type of a boolean value is 'bool'.


# ------------------------------------------------------------
# Creating Boolean Variables
# ------------------------------------------------------------

is_active = True
is_admin = False

print("is_active:", is_active)
print("is_admin:", is_admin)
print("Type:", type(is_active))


# ------------------------------------------------------------
# Boolean from Comparisons (Numbers)
# ------------------------------------------------------------

x = 20
y = 10

print("x > y:", x > y)  # True
print("x < y:", x < y)  # False


# ------------------------------------------------------------
# Boolean from Comparisons (Strings)
# ------------------------------------------------------------
# Strings are compared lexicographically (dictionary order)

a = "a"
b = "b"

print("'a' > 'b':", a > b)  # False
print("'a' < 'b':", a < b)  # True


# ------------------------------------------------------------
# The bool() Function
# ------------------------------------------------------------
# bool(value) converts a value into True or False

print("bool('Hi'):", bool("Hi"))  # True
print("bool(100):", bool(100))  # True
print("bool(0):", bool(0))  # False


# ------------------------------------------------------------
# Falsy Values
# ------------------------------------------------------------
# The following values evaluate to False:

print("bool(0):", bool(0))
print("bool(0.0):", bool(0.0))
print("bool(''):", bool(""))
print("bool([]):", bool([]))
print("bool(()):", bool(()))
print("bool({}):", bool({}))
print("bool(None):", bool(None))
print("bool(False):", bool(False))


# ------------------------------------------------------------
# Truthy Values
# ------------------------------------------------------------
# Any value that is NOT falsy is considered truthy.

print("bool(1):", bool(1))
print("bool(-10):", bool(-10))
print("bool('Hello'):", bool("Hello"))
print("bool([1, 2]):", bool([1, 2]))


# ------------------------------------------------------------
# Important Concept
# ------------------------------------------------------------
# In Python:
# - Boolean values are objects.
# - bool is a subclass of int.
#
# True behaves like 1
# False behaves like 0

print("True + True:", True + True)  # 2
print("True * 5:", True * 5)  # 5
print("False + 10:", False + 10)  # 10


# ------------------------------------------------------------
# Boolean in Conditions
# ------------------------------------------------------------

if is_active:
    print("User is active")

if not is_admin:
    print("User is not admin")
