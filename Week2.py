import numpy as np

a = np.array([2, 3, 4])

print(a)
print(a.dtype)

b = np.array([1.2, 3.5, 5.1])

print(b.dtype)
#Task 2: 2D & explicit types
c = np.array([[1, 2], [3, 4]], dtype=complex)
print(c)

#Task 3: Built-in array generators
zeros = np.zeros((3, 4))
ones = np.ones((2, 3), dtype=np.int16)
empty = np.empty((2, 3))

print(zeros)
print(ones)
print(empty)
# Task 4: arrange vs linspace
print(np.arange(10, 30, 5))
print(np.linspace(0, 2, 9))
# Floating point precision can cause rounding issues.
# linspace is safer because it creates exact points.
from numpy import pi

x = np.linspace(0, 2 * pi, 100)

y = np.sin(x)

print(y)
#Vector Operations
a = np.array([20, 30, 40, 50])

b = np.arange(4)
#Task 5: Elementwise arithmetic

print(a - b)

print(b ** 2)

print(10 * np.sin(a))
#Task 6: Matrix multiplication
A = np.array([[1, 1], [0, 1]])

B = np.array([[2, 0], [3, 4]])

print(A * B)

print(A @ B)
#Axis-Based Computation
b = np.arange(12).reshape(3, 4)

print(b)

print(b.sum(axis=0))     # column sums
print(b.min(axis=1))     # row minimums
print(b.cumsum(axis=1))  # cumulative sum

# axis=0 -> down columns
# axis=1 -> across rows
#Task 8: Slicing
a = np.arange(10) ** 3

print(a[2])
print(a[2:5])
print(a[:6:2])
print(a[::-1])

print(a[a > 100])
#Task 9 : 2D indexing
def f(x, y):
    return 10 * x + y


b = np.fromfunction(f, (5, 4), dtype=int)

print(b)

print(b[:, 1])

print(b[1:3, :])
#Task 10 : Shape operations
a = np.floor(10 * np.random.random((3, 4)))

print(a)

print(a.shape)

print(a.ravel())

print(a.reshape(6, 2))

print(a.T)

#Task 11: Stacking & splitting
print(np.vstack((a, a)))

print(np.hstack((a, a)))

print(np.hsplit(a, 2))
#Mini Case Study
sensor = np.array([
    [21.5, 22.1, 21.9],
    [20.9, 21.3, 21.0],
    [22.4, 22.8, 23.0]
])

print("Mean temperature per sensor:")
print(sensor.mean(axis=1))

print("Max temperature overall:")
print(sensor.max())

mean_temp = sensor.mean()

normalised = sensor - mean_temp

print("Normalised readings:")
print(normalised)

print("Readings greater than mean:")
print(sensor[sensor > mean_temp])
#Reflection and Discussion
# Reflection

# 1. Why is NumPy essential before pandas?
# NumPy provides fast numerical operations and
# forms the foundation of pandas.

# 2. Which operation replaced a loop?
# Vectorised operations replaced loops.

# 3. How does NumPy help machine learning?
# NumPy makes mathematical calculations fast
# and efficient for large datasets.

