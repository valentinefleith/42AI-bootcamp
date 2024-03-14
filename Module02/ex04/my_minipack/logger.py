# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    logger.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vafleith <vafleith@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/03/13 12:35:43 by vafleith          #+#    #+#              #
#    Updated: 2024/03/13 15:52:08 by vafleith         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import time
from random import randint
import os


def log(func):
    USERNAME = f"({os.getlogin()})"
    ACTION = func.__name__.replace('_', ' ').title()

    def inner(*args, **kwargs):
        called_at = time.time()
        to_execute = func(*args, **kwargs)
        exec_time = time.time() - called_at
        unit = 's'
        if (exec_time < 0.1):
            unit = 'ms'
            exec_time *= 1000
        instruction = f"{USERNAME}Running:\t{ACTION}\t[ exec-time = {exec_time:.3f} {unit} ]\n"
        with open("machine.log", "a") as file:
            file.write(instruction)
        return to_execute
    return inner


#... your definition of log decorator...
class CoffeeMachine():

    water_level = 100

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")

if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()
    machine.make_coffee()
    machine.add_water(70)
