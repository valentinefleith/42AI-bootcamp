# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#   ScrapBooker.py                                     :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#   By: vafleith <vafleith@student.42.fr>          +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#   Created: 2024/03/15 14:21:14 by vafleith          #+#    #+#              #
#   Updated: 2024/03/15 14:21:14 by vafleith         ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

from ImageProcessor import ImageProcessor
import numpy as np


class ScrapBooker:
    def crop(self, array, dim, position=(0,0)):
        """
        Crops the image as a rectangle via dim arguments (being the new height
        and width of the image) from the coordinates given by position arguments.
        Args:
        -----
            array: numpy.ndarray
            dim: tuple of 2 integers.
            position: tuple of 2 integers.
        Return:
        -------
            new_arr: the cropped numpy.ndarray.
            None (if combinaison of parameters not compatible).
        Raise:
        ------
            This function should not raise any Exception.
        """
        shape = np.shape(array)
        if position[0] + dim[0] > shape[0] or position[1] + dim[1] > shape[1]:
            return None
        cropped = array[position[0]:position[0] + dim[0], position[1]: position[1] + dim[1]]
        return cropped

    def thin(self, array, axis):
        """
        Deletes every n-th line pixels along the specified axis
        (0: vertical, 1: horizontal)
        Args:
        -----
            array: numpy.ndarray.
            n: non null positive integer lower than the number of row/column of the array
            (depending of axis value).
            axis: positive non null integer.
        Return:
        -------
            new_arr: thined numpy.ndarray.
            None (if combinaison of parameters not compatible).
        Raise:
        ------
            This function should not raise any Exception
        """
        pass


def main():
    imp = ImageProcessor()
    sb = ScrapBooker()
    arr = imp.load("42AI.png")
    cropped = sb.crop(arr, (100, 100), (50, 50))
    imp.display(cropped)


if __name__ == "__main__":
    main()
