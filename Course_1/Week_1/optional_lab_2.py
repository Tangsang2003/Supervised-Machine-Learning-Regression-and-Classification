import numpy as np
import matplotlib.pyplot as plt
# plt.style.use('./deeplearning.mplstyle')


def compute_model_output(x, weight, bias):
    m = x.shape[0]
    f_wb = np.zeros(m)
    for i in range(m):
        f_wb[i] = x[i] * weight + bias
    return f_wb


# x_train is a one dimensional numpy array and here it stores size in 1000 square feet.
x_train = np.array([1.0, 2.0])
# y stores price in thousands.
y_train = np.array([300.0, 500.0])
# numpy arrays have a .shape parameter that returns a tuple of dimensions. For example:
# it will return (3, 4) for a 2d array of 3 rows and 2 columns.
# m = x_train.shape[0]
# Use scatter function in matplotlib to plot points
plt.title('Housing Prices')
plt.xlabel('Size (1000 sq ft)')
plt.ylabel('Price ($1000)')
w = 500
b = 500
# for i in range(2):
#     x_i = x_train[i]
#     y_i = y_train[i]
#     plt.scatter(x_train, y_train, marker='x', c="r")
tmp_f_wb = compute_model_output(x_train, w, b,)

# Plot our model prediction
plt.plot(x_train, tmp_f_wb, c='b', label='Our Prediction')

# Plot the data points
plt.scatter(x_train, y_train, marker='x', c='r', label='Actual Values')

# Set the title
plt.title("Housing Prices")
# Set the y-axis label
plt.ylabel('Price (in 1000s of dollars)')
# Set the x-axis label
plt.xlabel('Size (1000 sq.ft)')
plt.legend()
plt.show()
