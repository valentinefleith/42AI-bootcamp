# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    book.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+     #
#    By: vafleith <vafleith@student.42.fr>          +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2024/03/12 16:22:02 by vafleith          #+#    #+#             #
#    Updated: 2024/03/12 17:27:20 by vafleith         ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

from datetime import datetime
from recipe import Recipe


class Book:
    def __init__(self, name: str):
        self.name = name
        self.creation_date = datetime.now()
        self.last_update = self.creation_date
        self.recipes_list = {"starter": [], "lunch": [], "dessert": []}

    def get_recipe_by_name(self, name) -> Recipe:
        for recipe_type in self.recipes_list.values():
            for recipe in recipe_type:
                if recipe and recipe.name == name:
                    print(str(recipe))
                    return recipe
        print("Recipe not found.")
        return None

    def get_recipes_by_types(self, recipe_type) -> list[str]:
        if recipe_type not in self.recipes_list.keys():
            print("Type has to be starter, lunch or dessert.")
            return None
        recipes = [
            recipe.name
            for recipe in self.recipes_list[recipe_type]
        ]
        return recipes

    def add_recipe(self, recipe) -> None:
        if not isinstance(recipe, Recipe):
            print("Wrong type. Given recipe has to be a Recipe.")
            return
        self.recipes_list[recipe.recipe_type].append(recipe)
        self.last_update = datetime.now()
