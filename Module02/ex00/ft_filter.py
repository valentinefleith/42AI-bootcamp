# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_filter.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+     #
#    By: vafleith <vafleith@student.42.fr>          +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2024/03/13 11:09:17 by vafleith          #+#    #+#             #
#    Updated: 2024/03/13 11:14:42 by vafleith         ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

def ft_filter(function_to_apply, iterable):
    """
    Filter the result of function apply to all elements of the iterable.
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
        if function_to_apply(element):
            yield element
