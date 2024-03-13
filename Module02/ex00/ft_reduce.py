# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_reduce.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+     #
#    By: vafleith <vafleith@student.42.fr>          +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2024/03/13 11:19:55 by vafleith          #+#    #+#             #
#    Updated: 2024/03/13 11:26:16 by vafleith         ###   ########.fr        #
#                                                                             #
# *************************************************************************** #


def ft_reduce(function_to_apply, iterable):
    """Apply function of two arguments cumulatively.
    Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
    Return:
    A value, of same type of elements in the iterable parameter.
    None if the iterable can not be used by the function.
    """
    if (
        not hasattr(iterable, "__iter__")
        or not callable(function_to_apply)
        or len(iterable) == 0
    ):
        return None
    result = iterable[0]
    for element in iterable[1:]:
        result = function_to_apply(result, element)
    return result
