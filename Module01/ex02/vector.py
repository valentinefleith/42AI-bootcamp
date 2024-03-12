# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    vector.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+     #
#    By: vafleith <vafleith@student.42.fr>          +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2024/03/12 18:04:40 by vafleith          #+#    #+#             #
#    Updated: 2024/03/12 20:14:52 by vafleith         ###   ########.fr        #
#                                                                             #
# *************************************************************************** #


class Vector:
    def __init__(self, values):
        self.values = self.process_values(values)
        self.shape = (
            (1, len(self.values))
            if self.is_row_vector(self.values)
            else (len(self.values), 1)
        )

    @staticmethod
    def process_values(values):
        if isinstance(values, list):
            if Vector.is_row_vector(values) or Vector.is_column_vector(values):
                return values
        if isinstance(values, int) and values > 0:
            return [[float(i)] for i in range(values)]
        if isinstance(values, tuple) and len(values) == 2:
            start, end = values
            if Vector.is_valid_range(start, end):
                return [[float(i)] for i in range(start, end)]
        raise ValueError("Invalid values")

    @staticmethod
    def is_row_vector(vector):
        if len(vector) != 1:
            return False
        return all(isinstance(elem, (int, float)) for elem in vector[0])

    @staticmethod
    def is_column_vector(vector):
        return all(
            isinstance(elem, list)
            and len(elem) == 1
            and isinstance(elem[0], (int, float))
            for elem in vector
        )

    @staticmethod
    def is_valid_size(value):
        return isinstance(value, int) and value > 0

    @staticmethod
    def is_valid_range(start, end):
        return isinstance(start, int) and isinstance(end, int) and start <= end

    def __str__(self):
        values = str(self.values)
        shape = str(self.shape)
        return values + '\n' + shape
