# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+     #
#    By: vafleith <vafleith@student.42.fr>          +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2024/03/12 16:22:09 by vafleith          #+#    #+#             #
#    Updated: 2024/03/12 16:55:10 by vafleith         ###   ########.fr        #
#                                                                             #
# *************************************************************************** #


class Recipe:
    @staticmethod
    def are_valid_attr(cooking_lvl, cooking_time, ingredients, recipe_type):
        if not 1 <= cooking_lvl <= 5:
            print("Cooking lvl has to be between 1 and 5.")
            return False
        if cooking_time < 0:
            print("Cooking time must be positive.")
            return False
        if len(ingredients) == 0:
            print("There must be ingredients.")
            return False
        if recipe_type not in ["starter", "lunch", "dessert"]:
            print("Recipe type must be starter, lunch or dessert.")
            return False
        return True

    def __init__(
        self,
        name: str,
        cooking_lvl: int,
        cooking_time: int,
        ingredients: list,
        description: str,
        recipe_type: str,
    ):
        if self.are_valid_attr(cooking_lvl, cooking_time, ingredients, recipe_type):
            self.name = name
            self.cooking_lvl = cooking_lvl
            self.cooking_time = cooking_time
            self.ingredients = ingredients
            self.description = description
            self.recipe_type = recipe_type
        else:
            raise Exception("Incorrect type.")

    def __str__(self):
        """Return the string to print with the recipe info"""
        name = f"The name of the recipe is {self.name}.\n"
        cooking_lvl = f"Its cooking lvl is {self.cooking_lvl}.\n"
        ingredients = f"Its ingredients are {self.ingredients}.\n"
        if self.description:
            description = f"Its description is : {self.description}.\n"
        else:
            description = ""
        recipe_type = f"Its type is {self.recipe_type}.\n"
        return name + cooking_lvl + ingredients + description + recipe_type
