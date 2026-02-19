# ------------------------------------------------------------
# Control Flow: for Loop with range()
# ------------------------------------------------------------
# A for loop is used to execute a block of code
# a fixed number of times.


# ------------------------------------------------------------
# 1. Basic for Loop with range(n)
# ------------------------------------------------------------
# range(n) generates numbers from 0 to n-1

for i in range(5):
    print("Index:", i)


# ------------------------------------------------------------
# 2. Printing 1 to 5 (Using range)
# ------------------------------------------------------------

# Method 1 (less clean)
for i in range(5):
    print(i + 1)

# Method 2 (recommended)
for i in range(1, 6):
    print(i)


# ------------------------------------------------------------
# 3. range(start, stop)
# ------------------------------------------------------------
# Starts from 'start' and goes up to (stop - 1)

for i in range(1, 6):
    print("Range 1 to 5:", i)


# ------------------------------------------------------------
# 4. range(start, stop, step)
# ------------------------------------------------------------
# 'step' controls increment

# Even numbers from 0 to 10
for i in range(0, 11, 2):
    print("Even:", i)

# Odd numbers (example)
for i in range(1, 11, 2):
    print("Odd:", i)


# ------------------------------------------------------------
# 5. Sum of Numbers (1 to 100)
# ------------------------------------------------------------

total = 0

for num in range(1, 101):
    total += num

print("Sum from 1 to 100:", total)


# ------------------------------------------------------------
# Mathematical Formula (Alternative)
# ------------------------------------------------------------

n = 100
formula_sum = n * (n + 1) // 2  # Using formula for sum of n numbers
print("Formula result:", formula_sum)


# ------------------------------------------------------------
# Important Notes
# ------------------------------------------------------------
# - range() does NOT include the stop value.
# - Default start = 0
# - Default step = 1
#
# range(5)       → 0,1,2,3,4
# range(1,6)     → 1,2,3,4,5
# range(0,11,2)  → 0,2,4,6,8,10


# ------------------------------------------------------------
# Advanced Insight (Important)
# ------------------------------------------------------------
# range() does NOT create a list.
# It returns a range object (lazy sequence).
# Computes the values when needed

r = range(5)
print("Range object:", r)
print("Convert to list:", list(r))
