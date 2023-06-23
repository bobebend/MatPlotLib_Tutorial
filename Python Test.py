import numpy as np
import pandas as pd


def max_of_rows(arr):
    max_values = np.max(arr, axis=1)
    return max_values
result = max_of_rows(np.array([[3, 4, 5], [6, 7, 8]]))
print(result)