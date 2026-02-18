# ------------------------------------------------------------
# Python Strings
# ------------------------------------------------------------
# A string is a sequence of characters.
# Anything inside quotes is considered a string in Python.
# You can use single or double quotes.


# ------------------------------------------------------------
# Creating Strings
# ------------------------------------------------------------

message1 = "This is a string in Python"
message2 = "This is also a string"

print(message1)
print(message2)


# If a string contains a single quote, use double quotes

message3 = "It's a string"
print(message3)


# If a string contains double quotes, use single quotes

message4 = '"Beautiful is better than ugly." Said Tim Peters'
print(message4)


# Escaping quotes using backslash (\)

message5 = "It's also a valid string"
print(message5)


# Raw strings (r prefix)
# Backslash is treated as a normal character

path = r"C:\python\bin"
print(path)


# ------------------------------------------------------------
# Multiline Strings (Triple Quotes)
# ------------------------------------------------------------

help_message = """
Usage: mysql command
    -h hostname
    -d database name
    -u username
    -p password
"""

print(help_message)


# ------------------------------------------------------------
# Using Variables in Strings (f-strings)
# ------------------------------------------------------------

name = "John"
message = f"Hi {name}"
print(message)

# f-strings were introduced in Python 3.6
# They allow variable interpolation inside strings.


# ------------------------------------------------------------
# String Concatenation
# ------------------------------------------------------------

# Adjacent string literals auto-concatenate

greeting = "Good Morning!"
print(greeting)


# Using + operator

greeting = "Good "
time = "Afternoon"

full_greeting = greeting + time + "!"
print(full_greeting)


# ------------------------------------------------------------
# Accessing String Characters (Indexing)
# ------------------------------------------------------------

text = "Python String"

print(text[0])  # First character
print(text[1])  # Second character

# Negative indexing (from end)

print(text[-1])  # Last character
print(text[-2])  # Second last character


# ------------------------------------------------------------
# Getting Length of String
# ------------------------------------------------------------

length = len(text)
print("Length:", length)


# ------------------------------------------------------------
# Slicing Strings
# ------------------------------------------------------------

print(text[0:2])  # From index 0 to 2 (2 excluded)
print(text[:6])  # From start to index 6
print(text[7:])  # From index 7 to end


# Syntax reminder:
# string[start:end]
# start is included
# end is excluded


# ------------------------------------------------------------
# Strings Are Immutable
# ------------------------------------------------------------

original = "Python String"

# The following code will cause an error because
# strings are immutable (cannot modify characters directly)

# original[0] = 'J'   # TypeError

# To modify a string, create a new one

new_string = "J" + original[1:]
print(new_string)


# ------------------------------------------------------------
# F-Strings with Expressions
# ------------------------------------------------------------

name = "Anthony"
age = 20

message = f"Hello, {name}! Next year you will be {age + 1}."
print(message)


# ------------------------------------------------------------
# Important Concept
# ------------------------------------------------------------
# Strings in Python are:
# - Objects
# - Immutable
# - Sequence types (support indexing and slicing)
#
# When you modify a string, Python creates a new string object.
