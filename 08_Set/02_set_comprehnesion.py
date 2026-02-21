# ------------------------------------------------------------
# Python Set Comprehension
# ------------------------------------------------------------

# Basic syntax:
# {expression for element in iterable}

# With condition:
# {expression for element in iterable if condition}


# ------------------------------------------------------------
# 1. Basic Transformation
# ------------------------------------------------------------

tags = {"Django", "Pandas", "Numpy"}

lowercase_tags = {tag.lower() for tag in tags}

print(lowercase_tags)


# ------------------------------------------------------------
# 2. With Condition
# ------------------------------------------------------------

# Exclude 'Numpy'
filtered_tags = {tag.lower() for tag in tags if tag != "Numpy"}

print(filtered_tags)


# ------------------------------------------------------------
# 3. From Any Iterable
# ------------------------------------------------------------

numbers = [1, 2, 2, 3, 4]

squares = {n * n for n in numbers}

print(squares)  # duplicates automatically removed


# ------------------------------------------------------------
# 4. Combined Transform + Filter
# ------------------------------------------------------------

numbers = [1, 2, 3, 4, 5, 6]

even_squares = {n * n for n in numbers if n % 2 == 0}

print(even_squares)
