# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ProportionBySport.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vafleith <vafleith@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/03/17 23:39:33 by vafleith          #+#    #+#              #
#    Updated: 2024/03/18 00:07:25 by vafleith         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import sys
from FileLoader import FileLoader


def proportion_by_sport(data, year, sport, gender):
    unique_participants = data.query("`Year` == @year and `Sex` == @gender")[
        ["Name", "Sport"]
    ].drop_duplicates(subset=["Name"])
    total = len(unique_participants)
    proportion = len(unique_participants.query("`Sport` == @sport")) / total
    return proportion


def main():
    if len(sys.argv) != 2:
        sys.exit("This program requires a csv file in argument.")
    loader = FileLoader()
    data = loader.load(sys.argv[1])
    print(proportion_by_sport(data, 2004, "Tennis", "F"))


if __name__ == "__main__":
    main()
