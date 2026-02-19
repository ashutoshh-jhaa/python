# ------------------------------------------------------------
# Functions: Keyword Arguments
# ------------------------------------------------------------
# Keyword arguments allow you to pass values using
# parameter names instead of relying on position.


# ------------------------------------------------------------
# 1. Basic Example (Positional Arguments)
# ------------------------------------------------------------


def get_net_price(price, discount):
    return price * (1 - discount)


print(get_net_price(100, 0.1))  # 90.0


# ------------------------------------------------------------
# Problem with Positional Arguments
# ------------------------------------------------------------
# Order matters → can lead to mistakes

print(get_net_price(0.1, 100))  # Wrong result


# ------------------------------------------------------------
# 2. Keyword Arguments
# ------------------------------------------------------------
# Syntax: function(param=value)

print(get_net_price(price=100, discount=0.1))
print(get_net_price(discount=0.1, price=100))  # Order doesn't matter


# ------------------------------------------------------------
# 3. Mixing Positional and Keyword Arguments
# ------------------------------------------------------------
# Positional arguments must come FIRST

print(get_net_price(100, discount=0.1))


# Invalid:
# print(get_net_price(price=100, 0.1))
# SyntaxError: positional argument follows keyword argument


# ------------------------------------------------------------
# 4. Keyword Arguments with Default Parameters
# ------------------------------------------------------------


def get_net_price_v2(price, tax_rate=0.07, discount=0.05):
    discounted_price = price * (1 - discount)
    net_price = discounted_price * (1 + tax_rate)
    return net_price


# Using all defaults
print(get_net_price_v2(100))


# ------------------------------------------------------------
# Problem Without Keywords
# ------------------------------------------------------------
# You cannot skip middle parameters using positional arguments

print(get_net_price_v2(100, 0.06))
# Here 0.06 is assigned to tax_rate, NOT discount


# ------------------------------------------------------------
# Fix Using Keyword Arguments
# ------------------------------------------------------------

print(get_net_price_v2(100, discount=0.06))  # Correct


# ------------------------------------------------------------
# 5. Important Rule
# ------------------------------------------------------------
# Once you use a keyword argument,
# all following arguments must also be keyword arguments.

# Invalid:
# get_net_price_v2(100, tax_rate=0.08, 0.06)

# Valid:
print(get_net_price_v2(100, tax_rate=0.08, discount=0.06))


# ------------------------------------------------------------
# Important Notes
# ------------------------------------------------------------
# - Keyword arguments improve readability
# - Order does not matter when using keywords
# - Useful when functions have many parameters
# - Helps avoid bugs from wrong argument order
