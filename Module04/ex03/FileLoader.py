# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    FileLoader.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vafleith <vafleith@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/03/17 17:43:18 by vafleith          #+#    #+#              #
#    Updated: 2024/03/17 18:00:23 by vafleith         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pandas as pd


class FileLoader:
    def load(self, path):
        df = pd.read_csv(path)
        rows, columns = df.shape
        print(f"Loading dataset of dimensions {rows} x {columns}")
        return df

    def display(self, df, n):
        if n >= 0:
            print(df.head(n))
        else:
            print(df.tail(-n))
