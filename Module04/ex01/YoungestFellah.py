# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    YoungestFellah.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vafleith <vafleith@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/03/17 18:06:17 by vafleith          #+#    #+#              #
#    Updated: 2024/03/17 23:35:42 by vafleith         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
from FileLoader import FileLoader
import pandas as pd


def youngest_fellah(df, year):
    youngest_male_age = df.query('`Sex` == "M" and `Year` == @year')[['Age']].min().to_list()
    youngest_female_age = df.query('`Sex` == "F" and `Year` == @year')[['Age']].min().to_list()
    return {'f': youngest_female_age[0], 'm': youngest_male_age[0]}


def main():
    if len(sys.argv) != 2:
        sys.exit("This program requires a csv file in argument.")
    loader = FileLoader()
    data = loader.load(sys.argv[1])
    print(youngest_fellah(data, 2004))


if __name__ == "__main__":
    main()
