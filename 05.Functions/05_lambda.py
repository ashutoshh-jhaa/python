# ------------------------------------------------------------
# Functions: Lambda (Anonymous Functions)
# ------------------------------------------------------------
# Lambda = small, one-line, unnamed function


# ------------------------------------------------------------
# 1. Basic Syntax
# ------------------------------------------------------------
# lambda parameters: expression

add = lambda a, b: a + b
print(add(2, 3))  # 5


# Equivalent normal function
def add_fn(a, b):
    return a + b


# ------------------------------------------------------------
# 2. When to Use Lambda
# ------------------------------------------------------------
# Use when:
# - Function is simple
# - Used only once
# - No need to define a full function


# ------------------------------------------------------------
# 3. Passing Function as Argument
# ------------------------------------------------------------


def get_full_name(first_name, last_name, formatter):
    return formatter(first_name, last_name)


# Using lambda instead of defining separate functions
print(get_full_name("John", "Doe", lambda f, l: f"{f} {l}"))

print(get_full_name("John", "Doe", lambda f, l: f"{l}, {f}"))


# ------------------------------------------------------------
# 4. Function Returning a Function
# ------------------------------------------------------------


def times(n):
    return lambda x: x * n


double = times(2)
print(double(5))  # 10

triple = times(3)
print(triple(5))  # 15


# ------------------------------------------------------------
# 5. Lambda in Loop (Important Trap)
# ------------------------------------------------------------

funcs = []
for i in range(3):
    funcs.append(lambda: i)

# All will print same value (last value of i)
for f in funcs:
    print(f())  # 2 2 2


# ------------------------------------------------------------
# Fix using default argument binding
# ------------------------------------------------------------

funcs = []
for i in range(3):
    funcs.append(lambda x=i: x)  # captures

for f in funcs:
    print(f())  # 0 1 2


# ------------------------------------------------------------
# Important Limitations
# ------------------------------------------------------------
# - Only ONE expression allowed
# - No statements (no loops, assignments, etc.)
# - Harder to read if overused


# ------------------------------------------------------------
# Summary
# ------------------------------------------------------------
# lambda = short, inline function
# use when function is simple and temporary
