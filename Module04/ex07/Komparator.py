# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Komparator.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vafleith <vafleith@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/03/19 20:32:48 by vafleith          #+#    #+#              #
#    Updated: 2024/03/19 20:53:50 by vafleith         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
from MyPlotLib import MyPlotLib
from FileLoader import FileLoader


class Komparator(MyPlotLib):

    def __init__(self, data):
        self.data = data

    def compare_box_plots(self, categorical_var, numerical_var):
        data = self.data[[categorical_var, numerical_var]].dropna()
        categories = data[categorical_var].unique()
        for i, category in enumerate(categories):
            self.box_plot(data.query(f"`{categorical_var}` == @category"), [numerical_var])


def main():
    if len(sys.argv) != 2:
        sys.exit("This program requires a csv file in argument.")
    loader = FileLoader()
    data = loader.load(sys.argv[1])
    kmp = Komparator(data)
    kmp.compare_box_plots("Sex", "Height")


if __name__ == "__main__":
    main()
    
