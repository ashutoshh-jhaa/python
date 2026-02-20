# ------------------------------------------------------------
# Lists: sorted() function
# ------------------------------------------------------------
# sorted() → returns a NEW sorted list (does NOT modify original)


# ------------------------------------------------------------
# 1. Basic Example (Numbers)
# ------------------------------------------------------------

scores = [5, 7, 4, 6, 9, 8]

sorted_scores = sorted(scores)

print("original:", scores)
print("sorted:", sorted_scores)


# ------------------------------------------------------------
# 2. Reverse Sorting
# ------------------------------------------------------------

sorted_scores = sorted(scores, reverse=True)
print("descending:", sorted_scores)


# ------------------------------------------------------------
# 3. Sorting Strings
# ------------------------------------------------------------

names = ["James", "Mary", "John", "Patricia", "Robert", "Jennifer"]

sorted_names = sorted(names)
print(sorted_names)

sorted_names_desc = sorted(names, reverse=True)
print(sorted_names_desc)


# ------------------------------------------------------------
# 4. Using key (same as sort())
# ------------------------------------------------------------

numbers = [-10, 5, -3]

print(sorted(numbers, key=abs))  # sort by absolute value


# ------------------------------------------------------------
# 5. Sorting Tuples
# ------------------------------------------------------------

students = [("ash", 20), ("john", 18), ("alex", 22)]

# sort by age
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)


# ------------------------------------------------------------
# 6. sorted() vs sort()
# ------------------------------------------------------------

nums = [3, 1, 2]

# sorted() → new list
new_nums = sorted(nums)

# sort() → modifies original
nums.sort()

print("after sort():", nums)
print("sorted() result:", new_nums)


# ------------------------------------------------------------
# Important Notes
# ------------------------------------------------------------
# - sorted() works on any iterable (list, tuple, string, etc.)
# - always returns a new list
# - does NOT change original data


# ------------------------------------------------------------
# Summary
# ------------------------------------------------------------
# - sorted(iterable) → new sorted list
# - reverse=True → descending
# - key=... → custom sorting logic
