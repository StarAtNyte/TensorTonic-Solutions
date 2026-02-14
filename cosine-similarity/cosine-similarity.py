import numpy as np
import math 

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    denominator  = (np.linalg.norm(a) * np.linalg.norm(b))
    if denominator == 0:
      return 0.0
    return (np.dot(a, b)) / denominator