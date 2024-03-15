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
    def crop(self, array, dim, position=(0, 0)):
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
        cropped = array[
            position[0] : position[0] + dim[0], position[1] : position[1] + dim[1]
        ]
        return cropped

    def thin(self, array, n, axis):
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
        arr_shape = np.shape(array)
        if (n > arr_shape[0] and axis == 0) or (n > arr_shape[1] and axis == 1):
            return None
        thin = np.delete(array, n, axis=axis)
        return thin

    def juxtapose(self, array, n, axis):
        """
        Juxtaposes n copies of the image along the specified axis.
        Args:
        -----
            array: numpy.ndarray.
            n: positive non null integer.
            axis: integer of value 0 or 1.
        Return:
        -------
            new_arr: juxtaposed numpy.ndarray.
            None (combinaison of parameters not compatible).
        Raises:
        -------
            This function should not raise any Exception.
        """
        if n < 0:
            return None
        new_arr = np.copy(array)
        if n == 0:
            return new_arr
        for _ in range(n):
            new_arr = np.concatenate((new_arr, array), axis=axis)
        return new_arr

    def mosaic(self, array, dim):
        """
        Makes a grid with multiple copies of the array. The dim argument specifies
        the number of repetition along each dimensions.
        Args:
        -----
            array: numpy.ndarray.
            dim: tuple of 2 integers.
        Return:
        -------
            new_arr: mosaic numpy.ndarray.
            None (combinaison of parameters not compatible).
        Raises:
        -------
            This function should not raise any Exception.
        """
        if any(dim) <= 0:
            return None
        horizontal = self.juxtapose(array, dim[0] - 1, 0)
        mosaic = self.juxtapose(horizontal, dim[1] - 1, 1)
        return mosaic


def main():
    imp = ImageProcessor()
    sb = ScrapBooker()
    arr = imp.load("42AI.png")
    ######### crop test #########
    # cropped = sb.crop(arr, (100, 100), (50, 50))
    # imp.display(cropped)
    ######### thin test #########
    # for _ in range(1, 100):
    #     arr = sb.thin(arr, 50, 1)
    #     if arr is None:
    #         break
    # imp.display(arr)
    ######## juxtapose test #########
    # juxtaposed = sb.juxtapose(arr, 2, 1)
    # imp.display(juxtaposed)
    ######## mosaic test #########
    mosaic = sb.mosaic(arr, (0, 1))
    imp.display(mosaic)


if __name__ == "__main__":
    main()
