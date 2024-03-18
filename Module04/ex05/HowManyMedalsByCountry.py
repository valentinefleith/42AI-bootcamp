# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    HowManyMedalsByCountry.py                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vafleith <vafleith@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/03/18 15:47:58 by vafleith          #+#    #+#              #
#    Updated: 2024/03/19 00:25:41 by vafleith         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import sys
import pandas as pd
from FileLoader import FileLoader


def count_medals(medal):
    def count(df):
        medal.title()
        return len(df.query("`Medal` == @medal"))

    return count


COUNTS = [count_medals("Gold"), count_medals("Silver"), count_medals("Bronze")]
KEYS = ["G", "S", "B"]
team_sport = [
    "Basketball",
    "Football",
    "Tug-Of-War",
    "Badminton",
    "Sailing",
    "Handball",
    "Water Polo",
    "Hockey",
    "Rowing",
    "Bobsleigh",
    "Softball",
    "Volleyball",
    "Synchronized Swimming",
    "Baseball",
    "Rugby Sevens",
    "Rugby",
    "Lacrosse",
    "Polo",
]


def how_many_medals_by_country(df, country):
    performances_by_country = df.query("`Team` == @country")[
        ["Team", "Medal", "Sport", "Year"]
    ]
    performances_team = performances_by_country.query(
        "`Sport` in @team_sport"
    ).drop_duplicates(subset="Sport")
    performances_solo = performances_by_country.query("`Sport` not in @team_sport")
    performances = pd.concat([performances_team, performances_solo])
    years = performances[["Year"]].drop_duplicates(subset=["Year"])["Year"].to_list()
    result = {}
    for year in years:
        data_per_year = performances.query("`Year` == @year")[["Medal"]]
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
    print(how_many_medals_by_country(data, "United States"))


if __name__ == "__main__":
    main()
