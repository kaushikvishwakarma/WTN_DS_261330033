import numpy as np

def numpy_exercise_2():
    # Create one dimensional array
    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
    
    print(f"Array: {arr}")
    print(f"Number of dimensions (ndim): {arr.ndim}")
    print(f"Shape: {arr.shape}")
    
    # Reshape operation: reshape to 3x3 array
    reshaped_arr = arr.reshape(3, 3)
    print(f"Reshaped Array:\n{reshaped_arr}")

if __name__ == "__main__":
    numpy_exercise_2()
