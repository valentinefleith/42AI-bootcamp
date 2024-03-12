# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    game.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+     #
#    By: vafleith <vafleith@student.42.fr>          +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2024/03/12 17:31:47 by vafleith          #+#    #+#             #
#    Updated: 2024/03/12 18:03:03 by vafleith         ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

class GotCharacter:
    def __init__(self, first_name: str = None, is_alive: bool = True):
        self.first_name = first_name
        self.is_alive = is_alive


class Stark(GotCharacter):
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is coming"

    def print_house_words(self):
        print(self.house_words)

    def die(self):
        self.is_alive = False


if __name__ == "__main__":
    arya = Stark("Arya")
    print(arya.__dict__)
    arya.print_house_words()
    print(arya.is_alive)
    arya.die()
    print(arya.is_alive)
