# Calculating Variance
import numpy as np


data = np.array([1,1,1,1,
                   2,2,2,2,
                   3,3,3,3,
                   4,4,4,4,
                   5,5,5,5,
                   6,6,6,6,
                   7,7,7,7,
                   8,8,8,8,
                   9,9,9,9,
                   10,10,10,10,
                   10,10,10,10,
                   10,10,10,10,
                   10,10,10,10,])
probabilities = np.array([0.01923,0.01923,0.01923,0.01923,
                   0.01923,0.01923,0.01923,0.01923,
                   0.01923,0.01923,0.01923,0.01923,
                   0.01923,0.01923,0.01923,0.01923,
                   0.01923,0.01923,0.01923,0.01923,
                   60.01923,0.01923,0.01923,0.01923,
                   0.01923,0.01923,0.01923,0.01923,
                   0.01923,0.01923,0.01923,0.01923,
                   0.01923,0.01923,0.01923,0.01923,
                   0.01923,0.01923,0.01923,0.01923,
                   0.01923,0.01923,0.01923,0.01923,
                   0.01923,0.01923,0.01923,0.01923,
                   0.01923,0.01923,0.01923,0.01923,])

expected_value = np.average(data, weights=probabilities)
print(f"Expected Value: {expected_value}")

population_variance = np.var(data)
print(f"Population Variance: {population_variance}")

sample_variance_np = np.var(data, ddof=1)
print(f"Sample Variance (NumPy): {sample_variance_np}")