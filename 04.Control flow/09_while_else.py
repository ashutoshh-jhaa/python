# ------------------------------------------------------------
# Python while...else
# ------------------------------------------------------------

# Basic syntax:
#
# while condition:
#     loop body
# else:
#     runs if loop ends normally


# ------------------------------------------------------------
# 1. Core Concept
# ------------------------------------------------------------

# else executes ONLY IF:
# - while condition becomes False
# - loop did NOT exit using break or return

# If break occurs → else is skipped.


# ------------------------------------------------------------
# 2. Mental Model
# ------------------------------------------------------------

# while → keep checking
# break → found / terminate early
# else → not found / normal completion

# Think:
# "If loop didn’t break, run else."


# ------------------------------------------------------------
# 3. Basic Example
# ------------------------------------------------------------

i = 0

while i < 3:
    print(i)
    i += 1
else:
    print("Loop finished normally")

# Condition becomes False → else runs


# ------------------------------------------------------------
# 4. break Skips else
# ------------------------------------------------------------

i = 0

while i < 5:
    if i == 2:
        break
    i += 1
else:
    print("Will NOT execute")

# break prevents else from running


# ------------------------------------------------------------
# 5. Practical Search Example
# ------------------------------------------------------------

basket = [
    {"fruit": "apple", "qty": 20},
    {"fruit": "banana", "qty": 30},
    {"fruit": "orange", "qty": 10},
]

fruit = "lemon"
index = 0

while index < len(basket):
    item = basket[index]

    if item["fruit"] == fruit:
        print(f"Basket has {item['qty']} {fruit}(s)")
        break

    index += 1
else:
    print("Fruit not found, adding it.")
    basket.append({"fruit": fruit, "qty": 15})

print(basket)

# No need for a flag variable.


# ------------------------------------------------------------
# 6. Equivalent Flag Version (Less Clean)
# ------------------------------------------------------------

found = False
index = 0

while index < len(basket):
    if basket[index]["fruit"] == fruit:
        found = True
        break
    index += 1

if not found:
    print("Not found")

# while...else eliminates this pattern.


# ------------------------------------------------------------
# 7. Important Rules
# ------------------------------------------------------------

# 1. else belongs to while, not to if.
# 2. Executes only if loop finishes naturally.
# 3. break or return prevents else.
# 4. Works like for...else.


# ------------------------------------------------------------
# 8. Performance Note
# ------------------------------------------------------------

# No performance overhead.
# Pure control-flow feature.
# Removes need for extra boolean flags.


# ------------------------------------------------------------
# 9. Common Mistakes
# ------------------------------------------------------------

# Mistake 1: Thinking else runs when condition is True
# It runs only after condition becomes False.

# Mistake 2: Expecting else after break

while True:
    break
else:
    print("Never runs")


# ------------------------------------------------------------
# 10. Key Insight
# ------------------------------------------------------------

# Use while...else for:
# - Search loops
# - Validation loops
# - Retry mechanisms

# Pattern:

# while condition:
#     if found:
#         break
# else:
#     handle_not_found
