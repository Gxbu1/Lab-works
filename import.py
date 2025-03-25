import numpy as np

# create a numpy array
np_array = np.array([1, 2, 3, 4, 5])
print("NumPy array:", np_array)

# basic operations with numpy arrays
print("Array + 2:", np_array + 2)
print("Array * 3:", np_array * 3)

# create a 2D array
np_2d_array = np.array([[1, 2, 3], [4, 5, 6]])
print("2D array:\n", np_2d_array)

# array properties
print("Shape:", np_2d_array.shape)
print("Dimensions:", np_2d_array.ndim)
print("Size:", np_2d_array.size)

# array manipulation
print("Transpose:\n", np_2d_array.T)
print("Flattened array:", np_2d_array.flatten())