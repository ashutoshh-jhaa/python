# ------------------------------------------------------------
# Python Iterables & Iterators
# ------------------------------------------------------------

# ------------------------------------------------------------
# 1. Iterable (WHAT you can loop over)
# ------------------------------------------------------------
# An iterable is any object you can loop through using a for loop

# Examples:
# list, tuple, string, range

numbers = [1, 2, 3]
for n in numbers:
    print(n)

# Rule:
# If "for x in something" works → it's an iterable


# ------------------------------------------------------------
# 2. Iterator (HOW looping actually happens)
# ------------------------------------------------------------
# Iterator is the object that keeps track of iteration state

numbers = [1, 2, 3]
it = iter(numbers)  # get iterator

print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # 3
# next(it) again → StopIteration error


# ------------------------------------------------------------
# 3. Key Difference (IMPORTANT)
# ------------------------------------------------------------

# Iterable:
# - collection (list, string, etc.)
# - can create multiple iterators

# Iterator:
# - moves step by step
# - remembers position (stateful)
# - gets exhausted


# ------------------------------------------------------------
# 4. What for-loop actually does internally
# ------------------------------------------------------------

numbers = [1, 2, 3]

# This:
for n in numbers:
    print(n)

# is roughly equal to:

it = iter(numbers)
while True:
    try:
        n = next(it)
        print(n)
    except StopIteration:
        break


# ------------------------------------------------------------
# 5. Important Behavior (STATEFUL)
# ------------------------------------------------------------

numbers = [1, 2, 3]
it = iter(numbers)

print(next(it))  # 1

# continue iteration
for n in it:
    print(n)
# prints: 2, 3

# iterator is now exhausted
for n in it:
    print(n)
# prints nothing


# ------------------------------------------------------------
# 6. Key Insight (VERY IMPORTANT)
# ------------------------------------------------------------

# Iterable = data source
# Iterator = pointer moving over data

# Think:
# list = book
# iterator = bookmark


# ------------------------------------------------------------
# Summary
# ------------------------------------------------------------
# Iterable → something you can loop over
# Iterator → object that performs the looping
# iter() → gives iterator
# next() → gives next value
# iterator is stateful and gets exhausted
