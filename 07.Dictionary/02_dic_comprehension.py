# ------------------------------------------------------------
# Python Dictionary Comprehension
# ------------------------------------------------------------

# Basic syntax:
# {key_expression: value_expression for key, value in dict.items()}

# With condition:
# {k: v for k, v in dict.items() if condition}


# ------------------------------------------------------------
# 1. Transforming a Dictionary
# ------------------------------------------------------------

stocks = {"AAPL": 121, "AMZN": 3380, "MSFT": 219}

# Increase each price by 2%
new_stocks = {symbol: price * 1.02 for symbol, price in stocks.items()}

print(new_stocks)


# ------------------------------------------------------------
# 2. Filtering a Dictionary
# ------------------------------------------------------------

# Keep only stocks with price > 200
filtered = {s: p for s, p in stocks.items() if p > 200}

print(filtered)


# ------------------------------------------------------------
# 3. Transform + Filter Together
# ------------------------------------------------------------

# Increase price by 2% only if > 200
updated = {s: p * 1.02 for s, p in stocks.items() if p > 200}

print(updated)


# ------------------------------------------------------------
# 4. Swapping Keys and Values
# ------------------------------------------------------------

original = {"a": 1, "b": 2, "c": 3}

swapped = {value: key for key, value in original.items()}

print(swapped)


# ------------------------------------------------------------
# 5. Creating Dictionary from List
# ------------------------------------------------------------

numbers = [1, 2, 3, 4]

squares = {n: n * n for n in numbers}

print(squares)
