# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_map.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+     #
#    By: vafleith <vafleith@student.42.fr>          +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2024/03/13 10:51:08 by vafleith          #+#    #+#             #
#    Updated: 2024/03/13 11:05:12 by vafleith         ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

def ft_map(function_to_apply, iterable):
    """
    Map the function to all elements of the iterable.
    Args:
        function_to_apply: a function taking an iterable.
        iterable: an iterable object (list, tuple, iterator).
    Return:
        an iterable.
        None if the iterable can not be used by the function.
    """
    if not hasattr(iterable, "__iter__") or not callable(function_to_apply):
        return None
    for element in iterable:
        yield function_to_apply(element)
