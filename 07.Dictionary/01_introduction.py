# ------------------------------------------------------------
# Python Dictionary
# ------------------------------------------------------------

# Dictionary = collection of key-value pairs
# syntax: {key: value}

# Keys:
# - must be immutable (str, int, tuple)
# - must be unique

# Values:
# - can be any type


# ------------------------------------------------------------
# 1. Creating Dictionary
# ------------------------------------------------------------

person = {"first_name": "John", "last_name": "Doe", "age": 25, "active": True}

empty_dict = {}


# ------------------------------------------------------------
# 2. Accessing Values
# ------------------------------------------------------------

print(person["first_name"])  # John

# Safer way (no KeyError)
print(person.get("age"))  # 25
print(person.get("ssn"))  # None
print(person.get("ssn", "N/A"))  # N/A


# ------------------------------------------------------------
# 3. Adding / Updating
# ------------------------------------------------------------

person["gender"] = "Male"  # add
person["age"] = 26  # update


# ------------------------------------------------------------
# 4. Removing
# ------------------------------------------------------------

del person["active"]

# safer removal
removed = person.pop("age", None)


# ------------------------------------------------------------
# 5. Looping
# ------------------------------------------------------------

# Keys (default)
for key in person:
    print(key)

# Values
for value in person.values():
    print(value)

# Key + Value
for key, value in person.items():
    print(key, value)


# ------------------------------------------------------------
# 6. Important Behavior
# ------------------------------------------------------------

# Dictionaries are:
# - mutable
# - ordered (Python 3.7+ preserves insertion order)
# - O(1) average lookup time


# ------------------------------------------------------------
# 7. Checking Existence
# ------------------------------------------------------------

if "first_name" in person:
    print("Exists")


# ------------------------------------------------------------
# 8. Dictionary Comprehension
# ------------------------------------------------------------

numbers = [1, 2, 3]

squares = {n: n * n for n in numbers}
print(squares)  # {1:1, 2:4, 3:9}
