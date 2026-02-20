# ------------------------------------------------------------
# Data Structures: List
# ------------------------------------------------------------
# A list is an ordered, mutable collection of items


# ------------------------------------------------------------
# 1. Creating Lists
# ------------------------------------------------------------

empty_list = []
numbers = [1, 3, 2, 7, 9, 4]
colors = ["red", "green", "blue"]

print(numbers)
print(colors)


# Nested list (list inside list)
coordinates = [[0, 0], [100, 100], [200, 200]]
print(coordinates)


# ------------------------------------------------------------
# 2. Accessing Elements
# ------------------------------------------------------------

numbers = [1, 3, 2, 7, 9, 4]

print(numbers[0])  # first element
print(numbers[1])  # second element

# Negative indexing
print(numbers[-1])  # last element
print(numbers[-2])  # second last


# ------------------------------------------------------------
# 3. Modifying Elements
# ------------------------------------------------------------

numbers = [1, 3, 2, 7, 9, 4]

numbers[0] = 10
print(numbers)

numbers[1] = numbers[1] * 10
print(numbers)

numbers[2] /= 2
print(numbers)


# ------------------------------------------------------------
# 4. Adding Elements
# ------------------------------------------------------------

numbers = [1, 3, 2, 7, 9, 4]

numbers.append(100)  # add at end
print(numbers)

numbers.insert(2, 100)  # insert at index
print(numbers)


# ------------------------------------------------------------
# 5. Removing Elements
# ------------------------------------------------------------

numbers = [1, 3, 2, 7, 9, 4]

# remove by index
del numbers[0]
print(numbers)


# pop last element
numbers = [1, 3, 2, 7, 9, 4]
last = numbers.pop()
print(last)
print(numbers)


# pop by index
numbers = [1, 3, 2, 7, 9, 4]
second = numbers.pop(1)
print(second)
print(numbers)


# remove by value (first occurrence only)
numbers = [1, 3, 2, 7, 9, 4, 9]
numbers.remove(9)
print(numbers)


# ------------------------------------------------------------
# Important Notes
# ------------------------------------------------------------
# - Lists are mutable (can change)
# - Can store mixed data types
# - Maintain order
# - Allow duplicates


# ------------------------------------------------------------
# Summary
# ------------------------------------------------------------
# - list[index] → access
# - list[index] = value → modify
# - append() → add at end
# - insert() → add at position
# - pop() → remove + return
# - remove() → remove by value
