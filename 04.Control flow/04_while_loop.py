# ------------------------------------------------------------
# Control Flow: while Loop
# ------------------------------------------------------------
# A while loop executes a block of code repeatedly
# as long as a condition is True.


# ------------------------------------------------------------
# 1. Basic while Loop
# ------------------------------------------------------------

counter = 0
max_value = 5

while counter < max_value:
    print("Counter:", counter)
    counter += 1  # Important: update condition variable


# ------------------------------------------------------------
# Important Concept
# ------------------------------------------------------------
# while is a "pre-test loop":
# - Condition is checked BEFORE execution
# - If condition is False initially → loop won't run


# ------------------------------------------------------------
# 2. Infinite Loop (Danger)
# ------------------------------------------------------------
# If you don't update the condition, the loop never stops.

# Example (DON'T RUN):
# while True:
#     print("Infinite loop")


# ------------------------------------------------------------
# 3. Controlled Loop with Condition
# ------------------------------------------------------------

num = 1

while num <= 5:
    print("Number:", num)
    num += 1


# ------------------------------------------------------------
# 4. User Input Loop (Simulated)
# ------------------------------------------------------------
# Normally uses input(), but we'll simulate it safely.

commands = ["hello", "test", "quit"]
i = 0

command = ""

while command != "quit":
    command = commands[i]
    print("Command:", command)
    i += 1


# ------------------------------------------------------------
# Real Version (Interactive)
# ------------------------------------------------------------
# Uncomment to try manually:

# command = ""
# while command.lower() != "quit":
#     command = input(">")
#     print(f"Echo: {command}")


# ------------------------------------------------------------
# Important Notes
# ------------------------------------------------------------
# - Always ensure the loop condition eventually becomes False
# - Otherwise → infinite loop
# - while loops are useful when number of iterations is unknown


# ------------------------------------------------------------
# Key Difference from for Loop
# ------------------------------------------------------------
# for loop  → fixed number of iterations
# while loop → runs until condition becomes False
