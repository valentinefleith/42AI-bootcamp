# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    loading.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+     #
#    By: vafleith <vafleith@student.42.fr>          +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2024/03/14 21:50:33 by vafleith          #+#    #+#             #
#    Updated: 2024/03/15 00:46:40 by vafleith         ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

import time


def ft_progress(iterator):
    BARSIZE = 30
    LENGTH = len(iterator)
    START_TIME = time.time()
    for i, elem in enumerate(iterator, 1):
        progress = i / LENGTH
        percentage = progress * 100
        pbar = ("=" * int(progress * (BARSIZE - 1))) + ">"
        elapsed = time.time() - START_TIME
        eta = elapsed / progress * (1 - progress)
        print(f"\rETA: {eta:.2f}s [{percentage:3.0f}%][{pbar:<{BARSIZE}}] {i}/{LENGTH} | elapsed time {elapsed:.2f}s", end="")
        yield elem


def main():
    listy = range(1000)
    ret = 0
    for elem in ft_progress(listy):
        ret += (elem + 3) % 5
        time.sleep(0.01)
    print()
    print(ret)


if __name__ == "__main__":
    main()
