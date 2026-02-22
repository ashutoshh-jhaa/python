# ------------------------------------------------------------
# Python try...except...else
# ------------------------------------------------------------

# Basic syntax:
#
# try:
#     risky code
# except SomeException:
#     handle error
# else:
#     runs if NO exception occurs


# ------------------------------------------------------------
# 1. Purpose of else
# ------------------------------------------------------------

# else runs ONLY when:
# - try block completes successfully
# - no exception was raised

# Mental Model:
# try   → attempt
# except → recover
# else  → success path


# ------------------------------------------------------------
# 2. Basic Example
# ------------------------------------------------------------

try:
    x = int(input("Enter a number: "))
except ValueError:
    print("Invalid input.")
else:
    print("Valid number:", x)

# If conversion fails → except runs
# If conversion succeeds → else runs


# ------------------------------------------------------------
# 3. Why Use else?
# ------------------------------------------------------------

# Keeps success logic separate from risky logic.
# Makes code cleaner and safer.

# Bad practice:
#
# try:
#     x = int(input())
#     print("Valid:", x)
# except ValueError:
#     print("Invalid")
#
# Here, print() is inside try unnecessarily.

# Better:
#
# try:
#     x = int(input())
# except ValueError:
#     print("Invalid")
# else:
#     print("Valid:", x)


# ------------------------------------------------------------
# 4. Control Flow Example (BMI)
# ------------------------------------------------------------


def calculate_bmi(height, weight):
    return weight / height**2


def evaluate_bmi(bmi):
    if 18.5 <= bmi <= 24.9:
        return "healthy"
    if bmi >= 25:
        return "overweight"
    return "underweight"


try:
    height = float(input("Height (m): "))
    weight = float(input("Weight (kg): "))
except ValueError:
    print("Please enter valid numbers.")
else:
    bmi = round(calculate_bmi(height, weight), 1)
    print("BMI:", bmi)
    print("Category:", evaluate_bmi(bmi))


# ------------------------------------------------------------
# 5. try...except...else...finally Order
# ------------------------------------------------------------

# Execution order:

# Case 1: No exception
# try → else → finally

# Case 2: Exception occurs
# try → except → finally


# Example:

try:
    x = 10 / 2
except ZeroDivisionError:
    print("Error")
else:
    print("Success:", x)
finally:
    print("Always runs")


# ------------------------------------------------------------
# 6. Important Rules
# ------------------------------------------------------------

# 1. else runs only if try succeeds completely.
# 2. else does NOT run if exception occurs.
# 3. finally always runs.
# 4. Only one except block executes.


# ------------------------------------------------------------
# 7. Common Mistakes
# ------------------------------------------------------------

# Mistake 1: Putting risky code in else

try:
    x = int("10")
except ValueError:
    pass
else:
    y = 10 / 0  # This will crash outside try

# Only code that depends on successful try
# should be inside else.


# Mistake 2: Thinking else is required
# It is optional.


# ------------------------------------------------------------
# 8. Performance Note
# ------------------------------------------------------------

# No extra performance cost.
# Purely for better structure and readability.


# ------------------------------------------------------------
# 9. Key Insight
# ------------------------------------------------------------

# Use else to separate:
# - error handling logic
# - normal execution logic

# Clean pattern:

# try → do risky operation
# except → handle failure
# else → continue safe operations
