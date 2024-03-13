# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    csvreader.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+     #
#    By: vafleith <vafleith@student.42.fr>          +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2024/03/13 15:56:08 by vafleith          #+#    #+#             #
#    Updated: 2024/03/14 00:04:34 by vafleith         ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

import sys


class CsvReader:
    def __init__(self, filename=None, sep=",", header=False, skip_top=0, skip_bottom=0):
        if filename is None:
            sys.exit("filename required.")
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        self.file_obj = open(self.filename, "r")
        self.data = self.parse_data()

    def parse_data(self):
        if is_corrputed(self.file_obj):
            return None
        data = []
        lines = self.file_obj.readlines()
        for i, line in enumerate(lines):
            if i < self.skip_top or i > len(lines) - self.skip_bottom:
                continue
            data.append([elem.strip() for elem in line.strip().split(self.sep)])
        return data

    def __enter__(self):
        # TODO : verify not corrputed here
        return self

    def __exit__(self, type, value, traceback):
        if self.file_obj is not None:
            self.file_obj.close()

    def getdata(self):
        """
        Retrieves the data/records from skip_top to skip_bottom.
        Return:
            nested list (list(list, list, ...)) representing the data.
        """
        data = []
        lines = self.file_obj.readlines()
        for i, line in enumerate(lines):
            if i < self.skip_top or i > len(lines) - self.skip_bottom:
                continue
            data.append([elem.strip() for elem in line.strip().split(self.sep)])
        return data


if __name__ == "__main__":
    with CsvReader('good.csv') as file:
        fdata = file.getdata()
        print(fdata)
