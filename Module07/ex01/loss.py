# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    loss.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vafleith <vafleith@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/03/20 23:56:36 by vafleith          #+#    #+#              #
#    Updated: 2024/03/27 16:20:57 by vafleith         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np


def are_valid(y, y_hat):
    if len(y) == 0 or len(y_hat) == 0:
        return False
    return len(y) == len(y_hat)


def loss_(y, y_hat):
    """
    Computes the half mean squared error of 2 non-empty np arrays, without
    any loop. The 2 arrays must have the same dimensions.
    Args:
        y: has to be a np.array
        y_hat: had to be a np.array
    Returns:
        The half mean squared error of the 2 vectors as a float.
        None if y or y_hat are empty.
        None if y and y_hat do not share the same dimensions.
    Raises:
        This function should not raise any Exceptions.
    """
    if not are_valid(y, y_hat):
        return None
    return np.mean(np.square(y - y_hat)) / 2


def main():
    X = np.array([[0], [15], [-9], [7], [12], [3], [-21]]).reshape((-1, 1))
    Y = np.array([[2], [14], [-13], [5], [12], [4], [-19]]).reshape((-1, 1))
    print(loss_(X, Y))
    print(loss_(X, X))


if __name__ == "__main__":
    main()
