# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    plot.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vafleith <vafleith@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/03/20 23:25:54 by vafleith          #+#    #+#              #
#    Updated: 2024/03/21 12:30:52 by vafleith         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
import matplotlib.pyplot as plt
from vec_loss import loss_
from prediction import predict_


def plot(x, y, theta):
    """
    Plot the data and prediction line from three non-empty np arrays.
    Args:
        x: has to be a np array, a vector of dimension m * 1.
        y: has to be a np array, a vector of dimension m * 1.
        theta: had to be a np array, a vector of dimension 2 * 1.
    Returns:
        Nothing
    Raises:
        This function should not raise any Exceptions.
    """
    if len(np.shape(x)) != 1 or len(np.shape(x)) != 1 or np.shape(theta) != (2, 1):
        return
    y_hat = predict_(x, theta).flatten()
    loss = loss_(y, y_hat)
    plt.scatter(x, y)
    plt.plot(x, theta[1] * x + theta[0], color="orangered")
    for i, datapoint in enumerate(x):
        plt.plot([datapoint, datapoint], [y[i], y_hat[i]], color="red", linestyle="--", linewidth=0.8)
    plt.title(f"Cost: {loss}")
    plt.show()


def main():
    x = np.arange(1, 6)
    y = np.array([3.74013816, 3.61473236, 4.57655287, 4.66793434, 5.95585554])
    theta1 = np.array([[4.5], [-0.2]])
    plot(x, y, theta1)
    theta2 = np.array([[-1.5], [2]])
    plot(x, y, theta2)
    theta3 = np.array([[3], [0.3]])
    plot(x, y, theta3)


if __name__ == "__main__":
    main()
