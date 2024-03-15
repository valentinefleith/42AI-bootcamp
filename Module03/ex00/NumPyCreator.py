# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    NumPyCreator.py                                    :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: vafleith <vafleith@student.42.fr>         +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2024/03/15 13:33:19 by vafleith         #+#    #+#              #
#    Updated: 2024/03/15 13:54:36 by vafleith         ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

import numpy as np


class NumPyCreator:
    def from_list(self, lst, dtype=None):
        """
        Takes a list or nested lists and returns its corresponding Np array.
        """
        return np.array(lst, dtype=dtype)

    def from_tuple(self, tpl, dtype=None):
        """
        Takes a tuple or nested tuples and returns its corresponding Np array.
        """
        return np.array(tpl, dtype=dtype)

    def from_iterable(self, itr, dtype=None):
        """
        Takes an iterable and returns an array which contains all its elements.
        """
        return np.array(itr, dtype=dtype)

    def from_shape(self, shape, value=0, dtype=None):
        """
        Returns an array filled with the same value.
        The first arg is a tuple which specifies the shape of the array.
        The second specifies the value of the elements.
        """
        return np.full(shape, value, dtype=dtype)

    def random(self, shape, dtype=None):
        """
        Returns an array filled with random values.
        It takes as an argument a tuple which specifies the shape fo the array.
        """
        return np.empty(shape, dtype=dtype)

    def identity(self, n, dtype=None):
        """
        Returns an array representing the identity matrix of size n.
        """
        return np.identity(n, dtype=dtype)
