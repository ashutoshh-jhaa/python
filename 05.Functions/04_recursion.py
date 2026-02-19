# ------------------------------------------------------------
# Functions: Recursion
# ------------------------------------------------------------
# A recursive function is a function that calls itself.


# ------------------------------------------------------------
# 1. Basic Concept
# ------------------------------------------------------------
# A recursive function must have:
# 1. Base case (stopping condition)
# 2. Recursive call (function calling itself)


# ------------------------------------------------------------
# 2. Simple Example: Countdown
# ------------------------------------------------------------


def count_down(n):
    print(n)

    # Base case
    if n <= 1:
        return

    # Recursive call
    count_down(n - 1)


count_down(3)


# ------------------------------------------------------------
# What Happens Internally
# ------------------------------------------------------------
# count_down(3)
# → print(3)
# → count_down(2)
# → print(2)
# → count_down(1)
# → print(1)
# → stop


# ------------------------------------------------------------
# 3. Infinite Recursion (Danger)
# ------------------------------------------------------------

# def bad_recursion(n):
#     print(n)
#     bad_recursion(n - 1)
#
# This will cause:
# RecursionError: maximum recursion depth exceeded


# ------------------------------------------------------------
# 4. Example: Sum of Numbers (1 to n)
# ------------------------------------------------------------


def sum_recursive(n):
    if n == 0:
        return 0

    return n + sum_recursive(n - 1)


print("Sum:", sum_recursive(100))


# ------------------------------------------------------------
# 5. Same Using Ternary (Compact)
# ------------------------------------------------------------


def sum_recursive_short(n):
    return n + sum_recursive_short(n - 1) if n > 0 else 0


print("Sum (short):", sum_recursive_short(100))


# ------------------------------------------------------------
# Important Concepts
# ------------------------------------------------------------
# - Base case → stops recursion
# - Recursive case → reduces problem
# - Each call adds a new stack frame
# - Too many calls → RecursionError


# ------------------------------------------------------------
# When to Use Recursion
# ------------------------------------------------------------
# - Problems that can be broken into smaller subproblems
# - Trees, graphs
# - Divide and conquer algorithms
#
# Example patterns:
# factorial, fibonacci, tree traversal
