# ------------------------------------------------------------
# Functions in Python
# ------------------------------------------------------------
# A function is a reusable block of code that performs a task
# or returns a value.


# ------------------------------------------------------------
# 1. Defining a Function
# ------------------------------------------------------------


def greet():
    """Display a greeting"""
    print("Hi")


# Calling the function
greet()


# ------------------------------------------------------------
# 2. Function with Parameters
# ------------------------------------------------------------
# Parameters are inputs to the function


def greet_user(name):
    print(f"Hi {name}")


greet_user("John")
greet_user("Alice")


# ------------------------------------------------------------
# 3. Parameters vs Arguments
# ------------------------------------------------------------
# Parameter → defined in function
# Argument → value passed during function call


def say_hello(name):  # 'name' is parameter
    print(f"Hello {name}")


say_hello("Ash")  # "Ash" is argument


# ------------------------------------------------------------
# 4. Returning Values
# ------------------------------------------------------------
# Functions can return values using 'return'


def greet_return(name):
    return f"Hi {name}"


message = greet_return("John")
print(message)


# ------------------------------------------------------------
# 5. Function with Multiple Parameters
# ------------------------------------------------------------


def add(a, b):
    return a + b


result = add(10, 20)
print("Sum:", result)


# ------------------------------------------------------------
# 6. Important Concept
# ------------------------------------------------------------
# After 'return', function execution stops


def test():
    print("Before return")
    return 10
    print("This will never run")  # unreachable


print("Returned value:", test())


# ------------------------------------------------------------
# 7. Functions Improve Code
# ------------------------------------------------------------
# - Reusability
# - Readability
# - Maintainability
