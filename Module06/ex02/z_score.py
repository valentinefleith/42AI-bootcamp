# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    z_score.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vafleith <vafleith@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/03/26 18:19:48 by vafleith          #+#    #+#              #
#    Updated: 2024/03/26 18:27:07 by vafleith         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np

def zscore(x):
    """
        Computes the normalized version of a non-empty numpy.ndarray using the z-score standardization.
        Args:
        x: has to be an numpy.ndarray, a vector.
        Returns:
        x’ as a numpy.ndarray.
        None if x is a non-empty numpy.ndarray or not a numpy.ndarray.
        Raises:
        This function shouldn’t raise any Exception.
    """
    x_prime = np.copy(x)
    return (x_prime - np.mean(x)) / np.std(x)


def main():
    X = np.array([0, 15, -9, 7, 12, 3, -21])
    print(zscore(X))
    Y = np.array([2, 14, -13, 5, 12, 4, -19]).reshape((-1, 1))
    print(zscore(Y))


if __name__ == "__main__":
    main()
