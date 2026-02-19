# ------------------------------------------------------------
# Control Flow: break Statement
# ------------------------------------------------------------
# The break statement is used to exit a loop immediately,
# regardless of the loop condition.


# ------------------------------------------------------------
# 1. break with for Loop
# ------------------------------------------------------------

for i in range(10):
    print("i:", i)

    if i == 3:
        break  # Exit loop when i == 3


# Output:
# 0 1 2 3 (then stops)


# ------------------------------------------------------------
# 2. break in Nested Loops
# ------------------------------------------------------------
# break only exits the innermost loop

for x in range(3):
    for y in range(3):
        if y == 2:
            break  # breaks inner loop only
        print(f"({x}, {y})")


# ------------------------------------------------------------
# 3. break with while Loop
# ------------------------------------------------------------

counter = 0

while True:
    print("Counter:", counter)
    counter += 1

    if counter == 3:
        break  # exit loop


# ------------------------------------------------------------
# 4. Simulated Input Example
# ------------------------------------------------------------
# Instead of real input(), we simulate it

inputs = ["red", "green", "quit"]
i = 0

while True:
    value = inputs[i]
    print("Input:", value)

    if value.lower() == "quit":
        break

    i += 1


# ------------------------------------------------------------
# Real Version (Interactive)
# ------------------------------------------------------------
# Uncomment to try:

# print("-- Type 'quit' to exit --")
# while True:
#     color = input("Enter color: ")
#     if color.lower() == "quit":
#         break


# ------------------------------------------------------------
# Important Notes
# ------------------------------------------------------------
# - break exits the loop immediately
# - Works in both for and while loops
# - In nested loops, it only breaks the inner loop
#
# Common use cases:
# - Stop loop when condition is met
# - Exit infinite loops safely
