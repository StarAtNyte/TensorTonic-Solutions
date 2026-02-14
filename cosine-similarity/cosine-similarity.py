import numpy as np
import math 

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    numerator = np.dot(a,b)
    denominator =  norm(a) * norm(b)
    if denominator == 0:
      return 0.0
    return numerator/denominator
    pass

def norm(vector):
  sum = 0
  for item in vector:
    sum += item **2
  return math.sqrt(sum)