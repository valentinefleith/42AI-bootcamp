# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ImageProcessor.py                                  :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: vafleith <vafleith@student.42.fr>         +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2024/03/15 14:04:31 by vafleith         #+#    #+#              #
#    Updated: 2024/03/15 14:13:36 by vafleith         ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

import numpy as np
import matplotlib.pyplot as plt


class ImageProcessor:
    def load(self, path):
        arr = plt.imread(path)
        shape = np.shape(arr)
        print(f"Loading image of dimensions {shape[0]} x {shape[1]}")
        return arr

    def display(self, array):
        image = plt.imshow(array)
        plt.show()


def main():
    imp = ImageProcessor()
    arr = imp.load("42AI.png")
    imp.display(arr)


if __name__ == "__main__":
    main()
