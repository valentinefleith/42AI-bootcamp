# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Komparator.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vafleith <vafleith@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/03/19 20:32:48 by vafleith          #+#    #+#              #
#    Updated: 2024/03/20 18:03:34 by vafleith         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import matplotlib.pyplot as plt
import pandas as pd
from MyPlotLib import MyPlotLib
from FileLoader import FileLoader


class Komparator(MyPlotLib):
    def __init__(self, data):
        self.data = data

    def compare_box_plots(self, categorical_var, numerical_var):
        data = self.data[[categorical_var, numerical_var]].dropna()
        categories = data[categorical_var].unique()
        _, ax = plt.subplots(ncols=len(categories))
        for i, category in enumerate(categories):
            ax[i].set_title(category)
            ax[i].boxplot(
                data.query(f"`{categorical_var}` == @category")[numerical_var]
            )
        plt.show()

    def compare_density(self, categorical_var, numerical_var):
        data = self.data[[categorical_var, numerical_var]].dropna()
        categories = data[categorical_var].unique()
        plt.figure()
        for category in categories:
            to_plot = data.query(f"`{categorical_var}` == @category")[numerical_var]
            to_plot.plot(kind="density", label=category)
        plt.legend()
        plt.xlabel(numerical_var)
        plt.show()

    def compare_histograms(self, categorical_var, numerical_var):
        data = self.data[[categorical_var, numerical_var]].dropna()
        categories = data[categorical_var].unique()
        plt.figure()
        for i, category in enumerate(categories):
            to_plot = data.query(f"`{categorical_var}` == @category")[numerical_var]
            plt.hist(to_plot, label=category, alpha=0.5)
        plt.xlabel(numerical_var)
        plt.ylabel("Frequency")
        plt.legend()
        plt.show()


def main():
    if len(sys.argv) != 2:
        sys.exit("This program requires a csv file in argument.")
    loader = FileLoader()
    data = loader.load(sys.argv[1])
    kmp = Komparator(data)
    # kmp.compare_box_plots("Sex", "Height")
    # kmp.compare_density("Sex", "Height")
    kmp.compare_histograms("Sex", "Height")


if __name__ == "__main__":
    main()
