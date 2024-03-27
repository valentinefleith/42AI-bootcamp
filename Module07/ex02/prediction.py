# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    prediction.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vafleith <vafleith@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/03/20 15:29:39 by vafleith          #+#    #+#              #
#    Updated: 2024/03/27 18:30:57 by vafleith         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np

def add_intercept(x):
    """
    Adds a column of 1's to the non-empty numpy.array x.
    Args:
        x: has to be a numpy.array of dimension m * n
    Returns:
        X, a numpy.array of dimension m * (n + 1)
        None if x is not a numpy.array.
        None if x is an empty numpy.array.
    Raises:
        This function should not raise any Exception.
    """
    if not isinstance(x, np.ndarray) or x.size == 0:
        return None
    x = np.column_stack((np.zeros(np.shape(x)[0]) + 1, x))
    return x


def predict_(x, theta):
    """Computes the prediction vector y_hat from two non-empty numpy.array.
    Args:
        x: has to be an numpy.array, a vector of dimensions m * n.
        theta: has to be an numpy.array, a vector of dimensions (n + 1) * 1.
    Return:
        y_hat as a numpy.array, a vector of dimensions m * 1.
        None if x or theta are empty numpy.array.
        None if x or theta dimensions are not appropriate.
        None if x or theta is not of expected type.
    Raises:
        This function should not raise any Exception.
    """
    x_prime = add_intercept(x)
    if x_prime is None:
        return None
    return np.dot(x_prime, theta)


def main():
    x = np.arange(1,13).reshape((4,-1))
    theta1 = np.array([5, 0, 0, 0]).reshape((-1, 1))
    print(predict_(x, theta1))
    theta2 = np.array([0, 1, 0, 0]).reshape((-1, 1))
    print(predict_(x, theta2))
    theta3 = np.array([-1.5, 0.6, 2.3, 1.98]).reshape((-1, 1))
    print(predict_(x, theta3))
    theta4 = np.array([-3, 1, 2, 3.5]).reshape((-1, 1))
    print(predict_(x, theta4))

if __name__ == "__main__":
    main()
