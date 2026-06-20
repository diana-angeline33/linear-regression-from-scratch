import numpy as np
import matplotlib.pyplot as plt

from linear_regression import fit
from linear_regression import predict

x = np.array([1,2,3,4])
y = np.array([40,50,60,70])

m, b, costs = fit(x, y)
print("m =", m)
print("b =", b)
print("Predictions =", predict(x, m, b))

y_line = predict(x, m, b)
plt.scatter(x, y)
plt.plot(x, y_line)
plt.xlabel("study hours")
plt.ylabel("test scores")
plt.title("Linear Regression from scratch")
plt.show()

plt.figure()
plt.plot(costs)
plt.xlabel("Iterations")
plt.ylabel("Cost")
plt.title("Learning curve")
plt.show()