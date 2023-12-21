# Importing necessary libraries
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model

# Defining the house prices and sizes
house_price = [245, 312, 279, 308, 199, 219, 405, 324, 319, 255]
size = [1400, 1600, 1700, 1875, 1100, 1550, 2350, 2450, 1425, 1700]

# Reshaping the 'size' array to a 2D array (needed for scikit-learn)
size2 = np.array(size).reshape((-1, 1))

# Creating a linear regression model
regr = linear_model.LinearRegression()

# Fitting the model with the size and house_price data
regr.fit(size2, house_price)

# Printing the coefficients and intercept of the model
print('Coefficients:', regr.coef_)
print('Intercept:', regr.intercept_)

# Defining a function for plotting the regression line
def graph(formula, x_range):
    x = np.array(x_range)
    y = eval(formula)
    plt.plot(x, y)

# Plotting the regression line using the coefficients and intercept
graph('regr.coef_*x + regr.intercept_', range(1000, 2700))

# Calculating and printing the R-squared value (model performance)
print('R-squared:', regr.score(size2, house_price))

# Plotting the scatter plot of size vs. house_price
plt.scatter(size, house_price, color='black')
plt.ylabel('House Price')
plt.xlabel('Size of House')

# Displaying the plot
plt.show()
