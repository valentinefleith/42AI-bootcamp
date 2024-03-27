# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    minmax.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vafleith <vafleith@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/03/27 15:14:34 by vafleith          #+#    #+#              #
#    Updated: 2024/03/27 15:22:56 by vafleith         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np


def minmax(x):
    """
        Computes the normalized version of a non-empty numpy.ndarray using the min-max standardization.
        Args:
            x: has to be an numpy.ndarray, a vector.
        Returns:
            x’ as a numpy.ndarray.
            None if x is a non-empty numpy.ndarray or not a numpy.ndarray.
        Raises:
            This function shouldn’t raise any Exception.
    """
    x_prime = np.copy(x)
    return (x_prime - np.min(x)) / (np.max(x) - np.min(x))


def main():
    X = np.array([0, 15, -9, 7, 12, 3, -21]).reshape((-1, 1))
    print(minmax(X))
    Y = np.array([2, 14, -13, 5, 12, 4, -19]).reshape((-1, 1))
    print(minmax(Y))


if __name__ == "__main__":
    main()
