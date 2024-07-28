import numpy as np

# Specifying data types
arr_int = np.array([10, 15, 32], dtype=np.int32)
arr_float = np.array([10.0, 15.0, 32.0], dtype=np.float64)

# Check the data type
print(arr_int)
print("Data type:",arr_int.dtype)
print(arr_float)
print("Data type:",arr_float.dtype)

# You can also specify the data type for individual elements
arr_custom = np.array([3, 2, 1], dtype=np.uint16)
print(arr_custom)
