# ------------------------------------------------------------
# Python for...else
# ------------------------------------------------------------

# Basic syntax:
#
# for item in iterable:
#     if condition:
#         break
# else:
#     runs if loop finishes WITHOUT break


# ------------------------------------------------------------
# 1. Core Concept
# ------------------------------------------------------------

# else executes ONLY IF:
# - Loop completes normally
# - No break statement executed

# else does NOT execute if:
# - break is triggered

# continue does NOT affect else.


# ------------------------------------------------------------
# 2. Mental Model
# ------------------------------------------------------------

# for → search / iterate
# break → found something
# else → not found

# Think:
# "If loop didn't break, run else."


# ------------------------------------------------------------
# 3. Basic Example
# ------------------------------------------------------------

numbers = [1, 2, 3, 4]
target = 5

for n in numbers:
    if n == target:
        print("Found")
        break
else:
    print("Not found")

# Since break never executed → else runs.


# ------------------------------------------------------------
# 4. Classic Search Pattern (Without Flag)
# ------------------------------------------------------------

people = [
    {"name": "John", "age": 25},
    {"name": "Jane", "age": 22},
    {"name": "Peter", "age": 30},
]

name = "Maria"

for person in people:
    if person["name"] == name:
        print(person)
        break
else:
    print(f"{name} not found")

# Cleaner than using a flag variable.


# ------------------------------------------------------------
# 5. Loop Over Empty Iterable
# ------------------------------------------------------------

items = []

for item in items:
    print(item)
else:
    print("Iterable is empty")

# Since loop never runs → else executes.


# ------------------------------------------------------------
# 6. continue vs break
# ------------------------------------------------------------

for i in range(3):
    if i == 1:
        continue
else:
    print("Loop completed")

# continue does NOT stop loop.
# No break occurred → else executes.


# ------------------------------------------------------------
# 7. Important Rules
# ------------------------------------------------------------

# 1. else is attached to the loop, NOT the if.
# 2. Executes only if loop completes naturally.
# 3. break skips else.
# 4. Works with both for and while loops.


# ------------------------------------------------------------
# 8. Performance Note
# ------------------------------------------------------------

# No performance overhead.
# Purely control-flow feature.
# Eliminates need for flag variables.


# ------------------------------------------------------------
# 9. Common Mistakes
# ------------------------------------------------------------

# Mistake 1: Thinking else belongs to if

for i in [1, 2]:
    if i == 3:
        break
else:
    print("Runs because no break")

# else is aligned with for, not if.


# Mistake 2: Expecting else to run after break

for i in [1, 2, 3]:
    if i == 2:
        break
else:
    print("Will NOT run")


# ------------------------------------------------------------
# 10. Key Insight
# ------------------------------------------------------------

# for...else is ideal for:
# - Search operations
# - Prime checking
# - Validation loops

# Pattern:

# for item in iterable:
#     if condition:
#         break
# else:
#     handle_not_found
