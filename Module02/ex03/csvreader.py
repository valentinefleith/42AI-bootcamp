# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    csvreader.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+     #
#    By: vafleith <vafleith@student.42.fr>          +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2024/03/13 15:56:08 by vafleith          #+#    #+#             #
#    Updated: 2024/03/14 01:13:14 by vafleith         ###   ########.fr        #
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
        self.file_obj = None
        self.data = []

    def __enter__(self):
        try:
            self.file_obj = open(self.filename, "r")
        except FileNotFoundError:
            return None
        content = self.file_obj.readlines()
        if len(content) == 0:
            return None
        line_length = len(content[0].split(self.sep))
        for _, line in enumerate(content):
            if len(line.split(self.sep)) != line_length:
                return None
        self.parse_data(content)
        return self

    def __exit__(self, type, value, traceback):
        if self.file_obj is not None:
            self.file_obj.close()

    def parse_data(self, content):
        for i, line in enumerate(content):
            if i < self.skip_top or i > len(content) - self.skip_bottom:
                continue
            self.data.append([elem.strip() for elem in line.strip().split(self.sep)])
        if self.header:
            self.header = [elem.strip() for elem in content[0].strip().split(self.sep)]

    def getdata(self):
        return self.data

    def getheader(self):
        return self.header


if __name__ == "__main__":
    with CsvReader("good.csv", header=True) as file:
        fdata = file.getdata()
        header = file.getheader()
        print(header)
        for line in fdata:
            print(line)
