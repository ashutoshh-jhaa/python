# ------------------------------------------------------------
# Python Type Conversion
# ------------------------------------------------------------
# Summary:
# Learn how to convert values from one type to another.


# ------------------------------------------------------------
# 1. input() Always Returns a String
# ------------------------------------------------------------

# Uncomment to test manually:
# value = input("Enter a value: ")
# print("You entered:", value)
# print("Type:", type(value))

# Important:
# input() returns a string, even if you enter numbers.


# ------------------------------------------------------------
# 2. Why Type Conversion Is Needed
# ------------------------------------------------------------

# Simulating user input (since input() is interactive)

price = "100"
tax = "10"

# This would cause an error:
# tax_amount = price * tax / 100
# TypeError: can't multiply sequence by non-int of type 'str'


# ------------------------------------------------------------
# 3. Converting String to Integer
# ------------------------------------------------------------

price_int = int(price)
tax_int = int(tax)

tax_amount = price_int * tax_int / 100
print("Tax amount:", tax_amount)


# ------------------------------------------------------------
# 4. Other Type Conversion Functions
# ------------------------------------------------------------

# Convert string to float
value_float = float("3.14")
print("Float:", value_float, type(value_float))

# Convert value to boolean
print("bool(1):", bool(1))
print("bool(0):", bool(0))

# Convert number to string
number = 500
number_str = str(number)
print("String:", number_str, type(number_str))


# ------------------------------------------------------------
# 5. Getting the Type of a Value
# ------------------------------------------------------------

print("Type of 100:", type(100))
print("Type of 2.0:", type(2.0))
print("Type of 'Hello':", type("Hello"))
print("Type of True:", type(True))


# ------------------------------------------------------------
# 6. Important Notes
# ------------------------------------------------------------
# - input() always returns str.
# - Use int(), float(), bool(), str() for conversion.
# - type(value) tells you the data type.
#
# In output, you see <class 'int'>, <class 'float'>, etc.
# This means every type in Python is a class.
