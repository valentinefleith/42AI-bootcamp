# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    tools.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vafleith <vafleith@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/03/20 15:29:39 by vafleith          #+#    #+#              #
#    Updated: 2024/03/20 16:08:12 by vafleith         ###   ########.fr        #
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


def main():
    x = np.arange(1, 6)
    print(add_intercept(x))
    y = np.arange(1, 10).reshape((3, 3))
    print(add_intercept(y))


if __name__ == "__main__":
    main()
