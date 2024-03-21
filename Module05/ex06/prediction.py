# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    prediction.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vafleith <vafleith@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/03/20 23:02:04 by vafleith          #+#    #+#              #
#    Updated: 2024/03/20 23:19:19 by vafleith         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
from tools import add_intercept


def are_valid(x, theta):
    if not isinstance(x, np.ndarray) or not isinstance(theta, np.ndarray):
        return False
    if len(x) == 0 or len(theta) == 0:
        return False
    return len(np.shape(x)) == 1 and np.shape(theta) == (2, 1)


def predict_(x, theta):
    """Computes the vector of prediction y_hat from 2 non-empty np arrays.
    Args:
        x: has to be a np array, a vector of dimension m * 1.
        theta: has to be an np array, a vector of dimension 2 * 1.
    Returns:
        y_hat as a np array, a vector of dimension m*1.
        None if x and/or theta are not numpy.array.
        None if x or theta are empty np arrays.
        None if x or theta dimensions are not appropriate.
    Raises:
        This function should not raise any Exceptions.
    """
    if not are_valid(x, theta):
        return None
    x = add_intercept(x)
    return np.dot(x, theta)


def main():
    x = np.arange(1, 6)
    theta1 = np.array([[5], [0]])
    print(predict_(x, theta1))
    theta2 = np.array([[0], [1]])
    print(predict_(x, theta2))
    theta3 = np.array([[5], [3]])
    print(predict_(x, theta3))
    theta4 = np.array([[-3], [1]])
    print(predict_(x, theta4))


if __name__ == "__main__":
    main()
