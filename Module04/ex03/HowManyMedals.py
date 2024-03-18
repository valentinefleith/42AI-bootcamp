# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    HowManyMedals.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vafleith <vafleith@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/03/18 15:47:58 by vafleith          #+#    #+#              #
#    Updated: 2024/03/18 23:14:04 by vafleith         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import sys
from FileLoader import FileLoader


def count_medals(medal):
    def count(df):
        medal.title()
        return len(df.query("`Medal` == @medal"))

    return count


COUNTS = [count_medals("Gold"), count_medals("Silver"), count_medals("Bronze")]
KEYS = ["G", "S", "B"]


def how_many_medals(df, name):
    performances_by_name = df.query("`Name` == @name")[["Name", "Medal", "Year"]]
    years = (
        performances_by_name[["Year"]]
        .drop_duplicates(subset=["Year"])["Year"]
        .to_list()
    )
    result = {}
    for year in years:
        data_per_year = performances_by_name.query("`Year` == @year")[["Medal"]]
        nb_medals = {}
        for count, key in zip(COUNTS, KEYS):
            nb_medals[key] = count(data_per_year)
        result[year] = nb_medals
    return result


def main():
    if len(sys.argv) != 2:
        sys.exit("This program requires a csv file in argument.")
    loader = FileLoader()
    data = loader.load(sys.argv[1])
    print(how_many_medals(data, "Kjetil Andr Aamodt"))


if __name__ == "__main__":
    main()
