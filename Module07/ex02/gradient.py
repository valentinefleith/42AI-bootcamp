# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    gradient.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vafleith <vafleith@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/03/23 22:57:39 by vafleith          #+#    #+#              #
#    Updated: 2024/03/27 16:34:23 by vafleith         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
from prediction import predict_


def simple_gradient(x, y, theta):
    """
        Computes a gradient vector from three non-empty numpy.array, without any for loop.
        The three arrays must have compatible shapes.
        Args:
            x: has to be a numpy.array, a matrix of shape m * 1. 
            y: has to be a numpy.array, a vector of shape m * 1.
            theta: has to be a numpy.array, a 2 * 1 vector.
        Return:
            The gradient as a numpy.ndarray, a vector of dimension 2 * 1.
            None if x, y, or theta is an empty numpy.ndarray.
            None if x, y and theta do not have compatible dimensions.
        Raises:
            This function should not raise any Exception.
    """
    y_hat = predict_(x, theta)
    if y_hat is None:
        return None
    grad = (1 / len(x)) * np.matmul(x_prime.T, y_hat - y)
    return grad


def main():
    x = np.array([12.4956442, 21.5007972, 31.5527382, 48.9145838, 57.5088733]).reshape((-1, 1))
    y = np.array([37.4013816, 36.1473236, 45.7655287, 46.6793434, 59.5585554]).reshape((-1, 1))
    theta1 = np.array([2, 0.7]).reshape((-1, 1))
    print(simple_gradient(x, y, theta1))
    theta2 = np.array([1, -0.4]).reshape((-1, 1))
    print(simple_gradient(x, y, theta2))


if __name__ == "__main__":
    main()
