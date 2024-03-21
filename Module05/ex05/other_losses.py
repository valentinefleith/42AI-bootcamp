# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    other_losses.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vafleith <vafleith@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/03/21 11:21:10 by vafleith          #+#    #+#              #
#    Updated: 2024/03/21 12:02:45 by vafleith         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np


def are_valid(y, y_hat):
    if len(np.shape(y)) != 1 or len(np.shape(y_hat)) != 1:
        if np.shape(y)[1] != 1 or np.shape(y_hat)[1] != 1:
            return False
    return np.shape(y)[0] == np.shape(y_hat)[0]


def mse_(y, y_hat):
    """
    Description:
        Calculates the MSE between the predicted output and the real output.
    Args:
        y: has to be an np.array, a vector of dimension m * 1.
        y_hat: has to be a np.array, a vector of dimension m * 1.
    Returns:
        mse: has to be a float.
        None if there is a matching dimension problem.
    """
    if not are_valid(y, y_hat):
        return None
    return np.mean(np.square(y - y_hat))

def rmse_(y, y_hat):
    """
    Description:
        Calculates the RMSE between the predicted output and the real output.
    Args:
        y: has to be an np.array, a vector of dimension m * 1.
        y_hat: has to be a np.array, a vector of dimension m * 1.
    Returns:
        mse: has to be a float.
        None if there is a matching dimension problem.
    """
    if not are_valid(y, y_hat):
        return None
    return np.sqrt(mse_(y, y_hat))

def mae_(y, y_hat):
    """
    Description:
        Calculates the MAE between the predicted output and the real output.
    Args:
        y: has to be an np.array, a vector of dimension m * 1.
        y_hat: has to be a np.array, a vector of dimension m * 1.
    Returns:
        mse: has to be a float.
        None if there is a matching dimension problem.
    """
    if not are_valid(y, y_hat):
        return None
    return np.mean(np.absolute(y - y_hat))

def r2score_(y, y_hat):
    """
    Description:
        Calculates the R2 score between the predicted output and the real output.
    Args:
        y: has to be an np.array, a vector of dimension m * 1.
        y_hat: has to be a np.array, a vector of dimension m * 1.
    Returns:
        mse: has to be a float.
        None if there is a matching dimension problem.
    """
    if not are_valid(y, y_hat):
        return None
    return 1 - np.sum((y - y_hat) ** 2) / np.sum((y - np.mean(y)) ** 2)


def main():
    X = np.array([0, 15, -9, 7, 12, 3, -21])
    Y = np.array([2, 14, -13, 5, 12, 4, -19])
    # X = np.array([[0], [15], [-9], [7], [12], [3], [-21]])
    # Y = np.array([[2], [14], [-13], [5], [12], [4], [-19]])
    print(mse_(X, Y))
    print(rmse_(X, Y))
    print(mae_(X, Y))
    print(r2score_(X, Y))


if __name__ == "__main__":
    main()
