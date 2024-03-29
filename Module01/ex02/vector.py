# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    vector.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+     #
#    By: vafleith <vafleith@student.42.fr>          +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2024/03/12 18:04:40 by vafleith          #+#    #+#             #
#    Updated: 2024/03/13 00:07:24 by vafleith         ###   ########.fr        #
#                                                                             #
# *************************************************************************** #


class Vector:
    def __init__(self, values):
        self.values = self.process_values(values)
        self.shape = (
            (1, len(self.values[0]))
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

    def __add__(self, other):
        if not (isinstance(other, Vector)) or self.shape != other.shape:
            raise ValueError("Vectors must have the same shapes")
        result_values = []
        for i in range(len(self.values)):
            row = []
            for j in range(len(self.values[i])):
                row.append(self.values[i][j] + other.values[i][j])
            result_values.append(row)
        return Vector(result_values)

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        if not (isinstance(other, Vector)) or self.shape != other.shape:
            raise ValueError("Vectors must have the same shapes.")
        result_values = []
        for i in range(len(self.values)):
            row = []
            for j in range(len(self.values[i])):
                row.append(self.values[i][j] - other.values[i][j])
            result_values.append(row)
        return Vector(result_values)

    def __rsub__(self, other):
        return other - self

    def __truediv__(self, scalar):
        if not isinstance(scalar, (float, int)):
            raise ValueError("Can only divide by float/int.")
        if float(scalar) == 0.0:
            raise ZeroDivisionError()
        result_values = []
        for i in range(len(self.values)):
            row = []
            for j in range(len(self.values[i])):
                row.append(self.values[i][j] / scalar)
            result_values.append(row)
        return Vector(result_values)

    def __rtruediv__(self, scalar):
        raise NotImplmentedError("Division of scalar by a Vector is not defined here.")

    def __mul__(self, scalar):
        if not isinstance(scalar, (float, int)):
            raise ValueError("Can only divide by float/int.")
        result_values = []
        for i in range(len(self.values)):
            row = []
            for j in range(len(self.values[i])):
                row.append(self.values[i][j] * scalar)
            result_values.append(row)
        return Vector(result_values)

    def __rmul__(self, scalar):
        return self * scalar

    def __str__(self):
        return f"Values: {self.values}\nShape: {self.shape}"

    def __repr__(self):
        return f"Values: {self.values}\nShape: {self.shape}"

    def dot(self, other):
        if not isinstance(other, Vector) or self.shape != other.shape:
            raise ValueError("Vectors must have the same shapes.")
        result = 0.0
        for i in range(len(self.values)):
            for j in range(len(self.values[i])):
                result += self.values[i][j] * other.values[i][j]
        return result

    def T(self):
        if self.shape[0] == 1:
            return Vector([[elem] for elem in self.values[0]])
        if self.shape[1] == 1:
            new = []
            for elem in self.values:
                new.extend(elem)
            return Vector([new])
        raise ValueError("Incorrect vector format.")
