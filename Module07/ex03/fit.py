# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    fit.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vafleith <vafleith@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/03/25 09:13:28 by vafleith          #+#    #+#              #
#    Updated: 2024/03/27 18:43:32 by vafleith         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
from gradient import gradient
from prediction import predict_


def fit_(x, y, theta, alpha, max_iter):
    """
    Description:
        Fits the model to the training dataset contained in x and y.
    Args:
        x: has to be a numpy.ndarray, a vector of dimension m * n.
        y: has to be a numpy.ndarray, a vector of dimension m * 1.
        theta: has to be a numpy.ndarray, a vector of dimension (n + 1) * 1.
        alpha: has to be a float, the learning rate
        max_iter: has to be an int, the number of iterations done during the gradient descent
    Returns:
        new_theta: numpy.ndarray, a vector of dimension (n + 1) * 1.
        None if there is a matching dimension problem.
    Raises:
        This function should not raise any Exception.
    """
    theta = theta.astype(float)
    for _ in range(max_iter):
        grad = gradient(x, y, theta)
        if grad is None:
            return gradient
        theta -= grad * alpha
    return theta


def main():
    x = np.array(
        [[0.2, 2.0, 20.0], [0.4, 4.0, 40.0], [0.6, 6.0, 60.0], [0.8, 8.0, 80.0]]
    )
    y = np.array([[19.6], [-2.8], [-25.2], [-47.6]])
    theta = np.array([[42.0], [1.0], [1.0], [1.0]])
    theta2 = fit_(x, y, theta, alpha=0.0005, max_iter=42000)
    print(theta2)
    print(predict_(x, theta2))


if __name__ == "__main__":
    main()
