import numpy as np
from linear_regression import predict

x = np.array([1, 2, 3, 4])

result = predict(x, 10, 30)

print(result)