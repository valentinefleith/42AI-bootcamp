# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    HowManyMedals.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vafleith <vafleith@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/03/18 15:47:58 by vafleith          #+#    #+#              #
#    Updated: 2024/03/18 23:57:44 by vafleith         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import sys
from FileLoader import FileLoader


class SpatioTemporalData:
    def __init__(self, data):
        self.data = data

    def when(self, location):
        return self.data.query("`City` == @location")[["Year"]].drop_duplicates(subset=["Year"])["Year"].to_list()

    def where(self, year):
        place = self.data.query("`Year` == @year")["City"].to_list()
        if len(place) >= 1:
            return place[0]
        return ""


def main():
    if len(sys.argv) != 2:
        sys.exit("This program requires a csv file in argument.")
    loader = FileLoader()
    data = loader.load(sys.argv[1])
    sp = SpatioTemporalData(data)
    print(sp.when("Paris"))
    print(sp.where(1896))


if __name__ == "__main__":
    main()
