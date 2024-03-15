# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ColorFilter.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vafleith <vafleith@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/03/15 17:24:38 by vafleith          #+#    #+#              #
#    Updated: 2024/03/15 19:48:06 by vafleith         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


from ImageProcessor import ImageProcessor
import numpy as np


class ColorFilter:
    def invert(self, array):
        """
        Inverts the color of the image received as a numpy array.
        Args:
        -----
            array: numpy.ndarray corresponding to the image.
        Return:
        -------
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
        -------
            This function should not raise any Exception.
        """
        inverted = np.copy(array)
        inverted[:, :, :3] = 255 - inverted[:, :, :3]
        return inverted

    def to_blue(self, array):
        """
        Applies a blue filter to the image received as a numpy array.
        Args:
        -----
            array: numpy.ndarray corresponding to the image.
        Return:
        -------
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
        -------
            This function should not raise any Exception.
        """
        blue_filter = np.copy(array)
        blue_filter[..., 0:2] = 0
        return blue_filter

    def to_green(self, array):
        """
        Applies a green filter to the image received as a numpy array.
        Args:
        -----
            array: numpy.ndarray corresponding to the image.
        Return:
        -------
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
        -------
            This function should not raise any Exception.
        """
        blue_filter = np.copy(array)
        blue_filter[..., :3:2] = array[..., :3:2] * 0
        return blue_filter

    def to_red(self, array):
        """
        Applies a red filter to the image received as a numpy array.
        Args:
        -----
            array: numpy.ndarray corresponding to the image.
        Return:
        -------
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
        -------
            This function should not raise any Exception.
        """
        red_filter = np.copy(array)
        only_blue_green = self.to_blue(red_filter) + self.to_green(red_filter)
        red_filter[..., :3] = red_filter[..., :3] - only_blue_green[..., :3]
        return red_filter


def main():
    imp = ImageProcessor()
    cf = ColorFilter()
    arr = imp.load("elon_canaGAN.png")
    arr = (arr * 255).astype(int)
    ##### INVERT TEST #####
    # inverted = cf.invert(arr)
    # imp.display(inverted)
    ##### BLUE TEST #####
    # blue_filter = cf.to_blue(arr)
    # imp.display(blue_filter)
    ##### GREEN TEST #####
    # green_filter = cf.to_green(arr)
    # imp.display(green_filter)
    ##### RED TEST #####
    red_filter = cf.to_red(arr)
    imp.display(red_filter)
    


if __name__ == "__main__":
    main()
