# ------------------------------------------------------------
# Python do...while Loop Emulation
# ------------------------------------------------------------

# Python does NOT support do...while natively.

# In other languages:
#
# do:
#     code
# while condition
#
# Executes at least once.
# Condition checked at END.


# ------------------------------------------------------------
# 1. Emulation Pattern in Python
# ------------------------------------------------------------

# Use infinite loop + break

while True:
    # code block

    # if exit_condition:
        # break

# Mental Model:
# Force first execution.
# Manually break when condition fails.


# ------------------------------------------------------------
# 2. Why Not Normal while?
# ------------------------------------------------------------

# Normal while checks condition FIRST.

# Example:

x = 5

while x < 5:
    print("Won't execute")

# Condition false → zero executions.


# ------------------------------------------------------------
# 3. Basic Emulation Example
# ------------------------------------------------------------

x = 0

while True:
    print("Runs at least once")

    x += 1
    if x >= 3:
        break

# Output runs 3 times.


# ------------------------------------------------------------
# 4. Practical Example (Number Guessing Game)
# ------------------------------------------------------------

from random import randint

MIN = 0
MAX = 10

secret_number = randint(MIN, MAX)
attempt = 0

while True:
    attempt += 1

    guess = int(input(f"Enter number between {MIN} and {MAX}: "))

    if guess > secret_number:
        print("Too high")
    elif guess < secret_number:
        print("Too low")
    else:
        print(f"Bingo in {attempt} attempts")
        break

# No duplicated code.
# Loop always executes at least once.


# ------------------------------------------------------------
# 5. Equivalent Logical Form
# ------------------------------------------------------------

# Conceptually this emulates:

# do:
#     code
# while condition

# Translated:

while True:
    # code

    if not condition:
        break


# ------------------------------------------------------------
# 6. Important Rules
# ------------------------------------------------------------

# 1. Must include break, otherwise infinite loop.
# 2. Condition is checked manually at bottom.
# 3. Always executes at least once.
# 4. Common in input-validation loops.


# ------------------------------------------------------------
# 7. Common Mistakes
# ------------------------------------------------------------

# Mistake 1: Forgetting break

while True:
    pass  # Infinite loop


# Mistake 2: Putting condition at top accidentally

while True:
    if False:
        break
    # Logic wrong → infinite loop


# ------------------------------------------------------------
# 8. Performance Note
# ------------------------------------------------------------

# Same performance as while loop.
# No extra overhead.
# Pure control-flow pattern.


# ------------------------------------------------------------
# 9. Key Insight
# ------------------------------------------------------------

# do...while pattern is ideal for:
# - User input validation
# - Menu-driven programs
# - Retry logic
# - Games

# Pattern to remember:

# while True:
#     do_something()
#     if stop_condition:
#         break
