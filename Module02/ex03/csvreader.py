# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    csvreader.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+     #
#    By: vafleith <vafleith@student.42.fr>          +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2024/03/13 15:56:08 by vafleith          #+#    #+#             #
#    Updated: 2024/03/13 16:32:29 by vafleith         ###   ########.fr        #
#                                                                             #
# *************************************************************************** #


class CsvReader:
    def __init__(self, filename=None, sep=",", header=False, skip_top=0, skip_bottom=0):
        if filename is None:
            exit("filename required.")
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        self.file_obj = open(self.filename, "r")

    def __enter__(self):
        # TODO : verify not corrputed here
        return self.file_obj

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
        for i in range(self.skip_bottom, len(self.file_obj.readlines())):
            data.append(self.file_obj.readlines()[i])
