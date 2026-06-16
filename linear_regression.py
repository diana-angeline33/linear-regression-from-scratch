import numpy as np


def predict(x, m, b):

    return m * x + b


def cost_function(y_true, y_pred):

    return np.mean((y_true - y_pred) ** 2)


def gradients(x, y, m, b):

    n = len(x)

    y_pred = predict(x, m, b)

    dm = (1/n) * np.sum((y_pred - y) * x)

    db = (1/n) * np.sum(y_pred - y)

    return dm, db

def fit(x, y, learning_rate=0.01, iterations=10000):

    m = np.random.randn()

    b = np.random.randn()

    for i in range(iterations):

        y_pred = predict(x, m, b)

        cost = cost_function(y, y_pred)

        dm, db = gradients(x, y, m, b)

        if abs(dm) < 0.001 and abs(db) < 0.001:

            print(f"Stopped at iteration {i}")

            break

        m = m - learning_rate * dm

        b = b - learning_rate * db

        if i % 1000 == 0:

            print(f"Iteration {i}: Cost = {cost}")

    return m, b