# ------------------------------------------------------------
# Control Flow: continue Statement
# ------------------------------------------------------------
# The continue statement skips the current iteration
# and moves to the next iteration of the loop.


# ------------------------------------------------------------
# 1. continue with for Loop
# ------------------------------------------------------------
# Print even numbers from 0 to 9

for i in range(10):
    if i % 2 != 0:
        continue  # Skip odd numbers

    print("Even:", i)


# ------------------------------------------------------------
# 2. continue with while Loop
# ------------------------------------------------------------
# Print odd numbers from 1 to 9

counter = 0

while counter < 10:
    counter += 1

    if counter % 2 == 0:
        continue  # Skip even numbers

    print("Odd:", counter)


# ------------------------------------------------------------
# Important Concept
# ------------------------------------------------------------
# continue does NOT stop the loop.
# It only skips the current iteration.


# ------------------------------------------------------------
# Difference: break vs continue
# ------------------------------------------------------------
# break    → exits the loop completely
# continue → skips current iteration and continues loop


# ------------------------------------------------------------
# Visual Understanding
# ------------------------------------------------------------
# Loop: 0 → 1 → 2 → 3 → 4
#
# With continue (skip even):
# 0(skip) → 1(print) → 2(skip) → 3(print) → 4(skip)


# ------------------------------------------------------------
# Common Use Cases
# ------------------------------------------------------------
# - Skipping unwanted values
# - Filtering data during iteration
# - Avoiding deeply nested conditions


# ------------------------------------------------------------
# Important Warning (while loop)
# ------------------------------------------------------------
# Be careful with continue in while loops.
# Always ensure the loop variable is updated BEFORE continue,
# otherwise it may cause an infinite loop.

# Example (DON'T DO THIS):
# counter = 0
# while counter < 5:
#     if counter == 2:
#         continue   # counter never updates when counter becomes 2 → infinite loop
#     counter += 1
