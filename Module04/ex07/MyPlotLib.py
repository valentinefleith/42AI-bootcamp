# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    MyPlotLib.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vafleith <vafleith@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/03/19 19:28:59 by vafleith          #+#    #+#              #
#    Updated: 2024/03/19 20:22:27 by vafleith         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import pandas as pd
import matplotlib.pyplot as plt
from FileLoader import FileLoader

class MyPlotLib:

    @staticmethod
    def histogram(data, features):
        _, ax = plt.subplots(ncols=len(features), figsize=(9, 5))
        for i, feature in enumerate(features):
            ax[i].set_title(feature)
            ax[i].hist(data[feature].dropna())
            ax[i].grid()
        plt.show()

    @staticmethod
    def density(data, features):
        pd.DataFrame(data[features]).plot(kind="density")
        plt.show()

    @staticmethod
    def pair_plot(data, features):
        pd.plotting.scatter_matrix(data[features])
        plt.show()

    @staticmethod
    def box_plot(data, features):
        _, ax = plt.subplots()
        ax.boxplot(data[features].dropna(), labels=features)
        plt.show()


def main():
    if len(sys.argv) != 2:
        sys.exit("This program requires a csv file in argument.")
    loader = FileLoader()
    data = loader.load(sys.argv[1])
    features = ["Weight", "Height"]
    mpl = MyPlotLib()
    # mpl.histogram(data, features)
    # mpl.density(data, features)
    # mpl.pair_plot(data, features)
    mpl.box_plot(data, features)


if __name__ == "__main__":
    main()
