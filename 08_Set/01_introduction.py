# ------------------------------------------------------------
# Python Set
# ------------------------------------------------------------

# Set = unordered collection of UNIQUE elements
# - no duplicates
# - elements must be immutable
# - mutable container

# ------------------------------------------------------------
# 1. Creating Sets
# ------------------------------------------------------------

skills = {"Python", "Databases", "Design"}

empty_set = set()  # {} creates dictionary, not set

# Remove duplicates automatically
letters = set("letter")
print(letters)  # {'l', 'e', 't', 'r'} (order not guaranteed)


# ------------------------------------------------------------
# 2. Properties
# ------------------------------------------------------------

# - unordered
# - no indexing
# - unique elements
# - mutable
# - O(1) average membership check


# ------------------------------------------------------------
# 3. Membership (Very Important)
# ------------------------------------------------------------

ratings = {1, 2, 3, 4}

print(1 in ratings)  # True
print(10 not in ratings)  # True


# ------------------------------------------------------------
# 4. Adding Elements
# ------------------------------------------------------------

skills.add("Problem Solving")


# ------------------------------------------------------------
# 5. Removing Elements
# ------------------------------------------------------------

skills.remove("Design")  # KeyError if not exists
skills.discard("Java")  # Safe, no error

item = skills.pop()  # Removes random element

skills.clear()  # Remove all elements


# ------------------------------------------------------------
# 6. Frozenset (Immutable Set)
# ------------------------------------------------------------

frozen = frozenset(skills)

# frozen.add('X')  -> Error


# ------------------------------------------------------------
# 7. Looping
# ------------------------------------------------------------

for skill in skills:
    print(skill)

for i, skill in enumerate(skills, 1):
    print(i, skill)
