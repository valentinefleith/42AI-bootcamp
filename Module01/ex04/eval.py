# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    eval.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+     #
#    By: vafleith <vafleith@student.42.fr>          +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2024/03/13 00:32:19 by vafleith          #+#    #+#             #
#    Updated: 2024/03/13 00:37:20 by vafleith         ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

class Evaluator:
    @staticmethod
    def zip_evaluate(coefs, words):
        if len(coefs) != len(words):
            return -1
        result = 0
        for coef, word in zip(coefs, words):
            result += coef * len(word)
        return result

    @staticmethod
    def enumerate_evaluate(coefs, words):
        if len(coefs) != len(words):
            return -1
        result = 0
        for i, word in enumerate(words):
            result += len(word) * coefs[i]
        return result
