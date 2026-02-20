# ------------------------------------------------------------
# Lists: sort() method
# ------------------------------------------------------------
# sort() → sorts the list in-place (modifies original list)


# ------------------------------------------------------------
# 1. Basic Sorting (Numbers)
# ------------------------------------------------------------

numbers = [5, 7, 4, 6, 9, 8]

numbers.sort()
print(numbers)  # [4, 5, 6, 7, 8, 9]


# Descending order
numbers.sort(reverse=True)
print(numbers)  # [9, 8, 7, 6, 5, 4]


# ------------------------------------------------------------
# 2. Sorting Strings
# ------------------------------------------------------------

names = ["James", "Mary", "John", "Patricia", "Robert", "Jennifer"]

names.sort()
print(names)

names.sort(reverse=True)
print(names)


# ------------------------------------------------------------
# 3. Important: sort() vs sorted()
# ------------------------------------------------------------

nums = [3, 1, 2]

# sort() → modifies original
nums.sort()
print(nums)

# sorted() → returns new list
nums = [3, 1, 2]
new_nums = sorted(nums)

print(nums)  # original unchanged
print(new_nums)  # new sorted list


# ------------------------------------------------------------
# 4. Sorting List of Tuples
# ------------------------------------------------------------

companies = [("Google", 2019, 134.81), ("Apple", 2019, 260.2), ("Facebook", 2019, 70.7)]


# Sort by revenue (index 2)
def sort_key(company):
    return company[2]


companies.sort(key=sort_key)
print(companies)


# ------------------------------------------------------------
# 5. Using Lambda (Cleaner)
# ------------------------------------------------------------

companies = [("Google", 2019, 134.81), ("Apple", 2019, 260.2), ("Facebook", 2019, 70.7)]

companies.sort(key=lambda c: c[2])
print(companies)


# Descending
companies.sort(key=lambda c: c[2], reverse=True)
print(companies)


# ------------------------------------------------------------
# 6. Key Insight (VERY IMPORTANT)
# ------------------------------------------------------------
# key=... does NOT sort directly
# It transforms each element before comparison

numbers = [10, -5, 3, -2]

# sort by absolute value
numbers.sort(key=abs)
print(numbers)  # [-2, 3, -5, 10]


# ------------------------------------------------------------
# Summary
# ------------------------------------------------------------
# - sort() → modifies list
# - sorted() → returns new list
# - key → decides HOW to compare
# - reverse=True → descending order
