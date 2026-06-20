#What I learned from implementing linear regression from scratch:

##Execution explaination:

* Import numpy for array operations
* Import matplotlib.pyplot for graph visualizations
* create a features numpy array ‘x’
* create a targets numpy array ‘y’
* initialize variables m & b with random values.

###define a new function named predict
→ return mx + b (uses numpy for computation)
→ let this returned value be called y_pred.

###define a new function named cost function
→ this function returns the mean squared error b/w the actual targets and the predicted targets.

###define a new function named gradients
→ let n be the total number of features.
→ let J be the equation for the cost function. so J becomes: [1/2 (y - (mx + b))^2], where y is the actual target and “mx + b” is the predicted target. For now we ignore the mean term “1/n Σ”.
⇒ To find dm (∂J/∂m) we can use chain rule
⇒ We substitute: (y - (mx + b)) = u
⇒ So, J becomes: J = 1/2 u^2
⇒ To find dm (∂J/∂m) we can use: ∂J/∂m = ∂J/∂u . ∂u/∂m
• ∂J/∂u = u
• ∂u/∂m = (-x)
• So, ∂J/∂m = u(-x)
∂J/∂m = (y - (mx + b))(-x)
∂J/∂m = (y - mx - b)(-x)
∂J/∂m = (mx + b - y)x
• Hence dm = (mx + b - y)x

⇒ To find db (∂J/∂b) we can use: ∂J/∂b = ∂J/∂u . ∂u/∂b
• ∂u/∂b = (-1)
• So, ∂J/∂b = u(-1)
∂J/∂b = -(y - (mx + b))
∂J/∂b = -(y - mx - b)
∂J/∂b = mx + b - y

⇒ After adding back the mean term “1/n Σ” and substituting “mx + b” with y-pred, we get:
• ∂J/∂m = dm = 1/n * np.sum((y-pred - y) * x)
• ∂J/∂b = db = 1/n * np.sum(y-pred - y)

→ The function accepts parameters: features, targets, target predictions, m and b, then returns the value of dm and db.

###define a new function named fit
→ it takes parameters: features, targets, learning rate (with default value 0.01), iterations (with default value 10000)
→ initialize empty list ‘cost’
→ loop through the number of iterations
⇒ calculates predicted targets, cost between actual value and predicted value, gradients dm and db.
→ loop is stopped if gradients dm and db become less than 0.001 (close to zero) and prints the iteration number at which it was stopped.
→ update the value of m and b so that the cost approaches zero. Subtract m and b with α_dm and α_db (learning rate multiplied with the gradient/slope)
→ Add the calculated value of the cost into the ‘costs’ list.
→ For every 1000th iteration print the value of cost for monitoring the training process.
→ return the final value of m, b and costs list.

###Final outputs
* print the final values of m and b.
* print the predictions calculated using m & b.

###Regression graph
* let y-line be the predicted targets.
* call the scatter function from matplotlib to convert coordinate data of the features & targets into visual points on a graph
* call the plot function to create a line passing through the feature points and the predicted target points.
* label x axis (feature) as “Study hours” and y axis (targets) as “test scores”
* Create the title for the graph “Linear Regression from scratch”
* Call the show function to display all the graphical objects created so far inside the figure. Matplotlib automatically creates a figure initially without explicit instruction.

###Learning curve
* Call the figure function to create a new figure to display the learning curve.
* Call the plot function to create a line passing through all the cost values. Matplotlib sets the cost values to be in the y axis and since x coordinates are not provided, it assumes x = [0, 1, 2, 3 …]
* Label x axis as “Iterations” (Assumed default values 0, 1, 2 …etc) and y axis as “Cost”
* Create the title for the graph as “Learning Curve”
* Call the show function to display all the graphical objects created so far inside the second figure.