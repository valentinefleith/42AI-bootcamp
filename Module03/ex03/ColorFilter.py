# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ColorFilter.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vafleith <vafleith@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/03/15 17:24:38 by vafleith          #+#    #+#              #
#    Updated: 2024/03/15 18:59:25 by vafleith         ###   ########.fr        #
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
        inverted = (inverted * 255).astype(int)
        inverted[:, :, :3] = 255 - inverted[:, :, :3]
        return inverted


def main():
    imp = ImageProcessor()
    cf = ColorFilter()
    arr = imp.load("elon_canaGAN.png")
    shape = np.shape(arr)
    print(shape)
    print(arr[100, 100])
    inverted = cf.invert(arr)
    imp.display(inverted)


if __name__ == "__main__":
    main()
