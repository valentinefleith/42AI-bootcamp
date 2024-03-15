# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    TinyStatistician.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+     #
#    By: vafleith <vafleith@student.42.fr>          +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2024/03/15 11:21:26 by vafleith          #+#    #+#             #
#    Updated: 2024/03/15 13:30:07 by vafleith         ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

class TinyStatistician:
    def mean(self, array):
        total = len(array)
        if total == 0:
            return None
        output = 0
        for elem in array:
            output += elem
        return output / total

    def median(self, array):
        total = len(array)
        if total == 0:
            return None
        array.sort()
        if total % 2 == 0:
            return (array[total // 2 - 1] + array[total // 2]) / 2
        return float(array[total // 2])

    def quartile(self, array):
        total = len(array)
        if total == 0:
            return None
        array.sort()
        if total % 2 == 0:
            quartile1 = (array[total // 4 - 1] + array[total // 4]) / 2
            quartile3 = (array[total // 4 * 3 - 1] + array[total // 4 * 3]) / 2
            return [quartile1, quartile3]
        return [float(array[total // 4]), float(array[total // 4 * 3])]

    def var(self, array):
        mean = self.mean(array)
        if mean is None:
            return mean
        deviations = [(val - mean) ** 2 for val in array]
        return sum(deviations) / len(array)

    def std(self, array):
        from math import sqrt
        var = self.var(array)
        if var is None:
            return None
        return sqrt(var)
