# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ColorFilter.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vafleith <vafleith@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/03/15 17:24:38 by vafleith          #+#    #+#              #
#    Updated: 2024/03/15 23:40:15 by vafleith         ###   ########.fr        #
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

    def to_celluloid(self, array):
        """
        Applies a celluloid filter to the image received as a numpy array.
        Celluloid filter must display at least four thresholds of shades.
        Be careful! You are not asked to apply black contour on the object,
        you only have to work on the shades of your images.
        Remarks:
        celluloid filter is also known as cel-shading or toon-shading.
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
        thresholds = np.linspace(array.min(), array.max(), 5)
        celluloid = np.copy(array)
        lower_threshold = thresholds[0]
        for upper_threshold in thresholds[:1]:
            mask = (celluloid[..., :3] > lower_threshold) & (
                celluloid[..., :3] < upper_threshold
            )
            celluloid[..., :3][mask] = lower_threshold
            lower_threshold = upper_threshold
        return celluloid

    def to_grayscale(self, array, filter, **kwargs):
        """
        Applies a grayscale filter to the image received as a numpy array.
        For filter = ’mean’/’m’: performs the mean of RBG channels.
        For filter = ’weight’/’w’: performs a weighted mean of RBG channels.
        Args:
        -----
            array: numpy.ndarray corresponding to the image.
            filter: string with accepted values in [’m’,’mean’,’w’,’weight’]
            weights: [kwargs] list of 3 floats where the sum equals to 1,
            corresponding to the weights of each RBG channels.
        Return:
        -------
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
        -------
            This function should not raise any Exception.
        """
        if filter not in ["m", "mean", "w", "weight"]:
            return None
        grayscale_filter = np.copy(array)
        if filter in ["m", "mean"]:
            grayscale_filter[..., 0:3] = np.sum(
                grayscale_filter[..., 0:3] / 3, axis=2, keepdims=True
            ).astype(grayscale_filter.dtype)
            return grayscale_filter
        weights = kwargs.get("weights")
        if len(weights) != 3:
            return None
        grayscale_filter[:, :, 0:3] = np.sum(
            [
                grayscale_filter[:, :, 0:1] * weights[0],
                weights[1] * array[:, :, 1:2],
                weights[2] * grayscale_filter[:, :, 2:3],
            ],
            axis=0,
        )
        return grayscale_filter


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
    # red_filter = cf.to_red(arr)
    # imp.display(red_filter)
    ##### CELLULOID TEST #####
    # celluloid_filter = cf.to_celluloid(arr)
    # imp.display(celluloid_filter)
    ##### GRAYSCALE TEST #####
    grayscale_filter = cf.to_grayscale(arr, "w", weights=[0.005, 0.05, 0.9])
    imp.display(grayscale_filter)


if __name__ == "__main__":
    main()
