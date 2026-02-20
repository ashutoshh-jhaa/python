# ------------------------------------------------------------
# Python filter() Function
# ------------------------------------------------------------

# filter() → selects elements based on a condition
# syntax: filter(function, iterable)


# ------------------------------------------------------------
# Basic Example
# ------------------------------------------------------------

scores = [70, 60, 80, 90, 50]

filtered = filter(lambda score: score >= 70, scores)
print(list(filtered))  # [70, 80, 90]


# ------------------------------------------------------------
# Equivalent using for loop (for understanding)
# ------------------------------------------------------------

scores = [70, 60, 80, 90, 50]

result = []
for score in scores:
    if score >= 70:
        result.append(score)

print(result)  # [70, 80, 90]


# ------------------------------------------------------------
# Important Concept
# ------------------------------------------------------------

# filter() returns an ITERATOR (lazy evaluation)

scores = [70, 60, 80, 90, 50]

filtered = filter(lambda x: x > 60, scores)

print(filtered)  # <filter object ...>
print(list(filtered))  # [70, 80, 90]


# ------------------------------------------------------------
# Example with complex data (list of lists / tuples)
# ------------------------------------------------------------

countries = [["India", 1326], ["USA", 329], ["Brazil", 211]]

# filter countries with population > 300
result = filter(lambda c: c[1] > 300, countries)

print(list(result))  # [['India', 1326], ['USA', 329]]


# ------------------------------------------------------------
# Pythonic Alternative (IMPORTANT)
# ------------------------------------------------------------

# list comprehension (more readable in most cases)

scores = [70, 60, 80, 90, 50]

filtered = [score for score in scores if score >= 70]
print(filtered)  # [70, 80, 90]


# ------------------------------------------------------------
# Key Insight
# ------------------------------------------------------------

# map()    → transforms every element
# filter() → selects some elements

# map:    x → f(x)
# filter: x → keep if condition(x)


# ------------------------------------------------------------
# Subtle Behavior (Iterator is consumed)
# ------------------------------------------------------------

scores = [70, 60, 80, 90, 50]

filtered = filter(lambda x: x >= 70, scores)

print(list(filtered))  # [70, 80, 90]
print(list(filtered))  # []  (already consumed)
