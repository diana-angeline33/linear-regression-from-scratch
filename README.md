#What I Learned from Implementing Linear Regression from Scratch

Execution Explanation

* Import numpy for array operations.
* Import matplotlib.pyplot for graph visualizations.
* Create a features NumPy array x.
* Create a targets NumPy array y.
* Initialize variables m and b with random values.

Define a New Function Named predict

* Return mx + b (uses NumPy for computation).
* Let this returned value be called y_pred.

Define a New Function Named cost_function

* This function returns the Mean Squared Error (MSE) between the actual targets and the predicted targets.

Define a New Function Named gradients

* Let n be the total number of features.
* Let J be the equation for the cost function:
    J = 1/2 (y - (mx + b))²
    where y is the actual target and mx + b is the predicted target.
* For now, ignore the mean term 1/n Σ.

Finding dm (∂J/∂m)

* Use the chain rule.
* Substitute:
    (y - (mx + b)) = u
* Therefore:
    J = 1/2 u²
* Apply the chain rule:
    ∂J/∂m = ∂J/∂u × ∂u/∂m
* Compute the derivatives:
    * ∂J/∂u = u
    * ∂u/∂m = -x
* Therefore:
    ∂J/∂m = u(-x)
    ∂J/∂m = (y - (mx + b))(-x)
    ∂J/∂m = (y - mx - b)(-x)
    ∂J/∂m = (mx + b - y)x
* Hence:
    dm = (mx + b - y)x

Finding db (∂J/∂b)

* Apply the chain rule:
    ∂J/∂b = ∂J/∂u × ∂u/∂b
* Compute:
    * ∂u/∂b = -1
* Therefore:
    ∂J/∂b = u(-1)
    ∂J/∂b = -(y - (mx + b))
    ∂J/∂b = -(y - mx - b)
    ∂J/∂b = mx + b - y

Adding Back the Mean Term

After adding back the mean term 1/n Σ and substituting mx + b with y_pred:

* dm = (1/n) × np.sum((y_pred - y) × x)
* db = (1/n) × np.sum(y_pred - y)
* The function accepts the parameters:
    * features (x)
    * targets (y)
    * target predictions (y_pred)
    * m
    * b
* The function returns dm and db.

Define a New Function Named fit

* Parameters:
    * features
    * targets
    * learning rate (default value: 0.01)
    * iterations (default value: 10000)
* Initialize an empty list named costs.
* Loop through the specified number of iterations.
    * Calculate predicted targets.
    * Calculate the cost between actual and predicted values.
    * Calculate gradients dm and db.
* Stop the loop if both dm and db become smaller than 0.001 (close to zero).
    * Print the iteration number at which training stopped.
* Update the values of m and b so that the cost approaches zero.
    * m = m - αdm
    * b = b - αdb
    where α is the learning rate.
* Add the calculated cost value to the costs list.
* Every 1000 iterations, print the current cost value to monitor training progress.
* Return:
    * final value of m
    * final value of b
    * costs list

Final Outputs

* Print the final values of m and b.
* Print the predictions calculated using m and b.

Regression Graph

* Let y_line be the predicted targets.
* Call the scatter() function from Matplotlib to convert the feature and target coordinate data into visual points on a graph.
* Call the plot() function to create a line passing through the feature points and predicted target points.
* Label the x-axis (feature) as “Study Hours”.
* Label the y-axis (target) as “Test Scores”.
* Create the graph title:
    “Linear Regression from Scratch”
* Call show() to display all graphical objects currently stored in the figure.
* Matplotlib automatically creates a figure if one does not already exist.

Learning Curve

* Call the figure() function to create a new figure for the learning curve.
* Call the plot() function to create a line passing through all cost values.
* Since x-values are not provided, Matplotlib automatically assumes:
    x = [0, 1, 2, 3, ...]
* Label the x-axis as “Iterations”.
* Label the y-axis as “Cost”.
* Create the graph title:
    “Learning Curve”
* Call show() to display all graphical objects in the second figure.