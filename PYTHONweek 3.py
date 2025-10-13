import numpy as np

# a. Help on the add function
help(np.add)

# b. Test whether none of the elements of a given array is zero
import numpy as np
arr1 = np.array([1, 2, 3, 4])
print("None of the elements is zero:", np.all(arr1 != 0))

# c. Element-wise comparison of two arrays
import numpy as np
arr2 = np.array([2, 2, 3, 5])

print("Greater:", np.greater(arr1, arr2))
print("Greater Equal:", np.greater_equal(arr1, arr2))
print("Less:", np.less(arr1, arr2))
print("Less Equal:", np.less_equal(arr1, arr2))
print("Equal:", np.equal(arr1, arr2))
print("Equal within tolerance:", np.allclose(arr1, arr2, atol=1))


# Convert to list
print("Array to list:", arr1.tolist())


2.

# Sample array
arr = np.array([[10, 20, 5], [30, 15, 25]])

# a. Extract numbers less than and greater than a specified number
specified_number = 18
less_than = arr[arr < specified_number]
greater_than = arr[arr > specified_number]
print("Less than 18:", less_than)
print("Greater than 18:", greater_than)

# b. Indices of max and min along axis
import numpy as np

# Create a sample 2D NumPy array
arr = np.array([[10, 20, 5],
                [15, 3, 25],
                [30, 8, 12]])

print("Original array:")
print(arr)

# Find the indices of the maximum values along each row (axis=1)
max_indices = np.argmax(arr, axis=1)

# Find the indices of the minimum values along each row (axis=1)
min_indices = np.argmin(arr, axis=1)

print("\nIndices of the maximum values along each row:", max_indices)
print("Indices of the minimum values along each row:", min_indices)

# To verify, you can use these indices to get the actual max and min values
max_values = arr[np.arange(len(arr)), max_indices]
min_values = arr[np.arange(len(arr)), min_indices]

print("\nMaximum values:", max_values)
print("Minimum values:", min_values)