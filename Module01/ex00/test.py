# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+     #
#    By: vafleith <vafleith@student.42.fr>          +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2024/03/12 16:47:50 by vafleith          #+#    #+#             #
#    Updated: 2024/03/12 17:28:54 by vafleith         ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

from book import Book
from recipe import Recipe


def main():
    cookbook = Book("My Cookbook")
    recipe = Recipe("Omelette", 1, 15, ["eggs", "cheese"], "eggs and cheese omelette", "lunch")
    cookbook.add_recipe(recipe)
    print(str(recipe))
    recipe = Recipe("Pizza", 4, 30, ["chicken", "cheese", "tomato sauce"], "Chicken and cheese pizza", "lunch")
    cookbook.add_recipe(recipe)
    print(str(recipe))
    recipe = Recipe("Chocolate cake", 2, 25, ["chocolate", "sugar", "eggs", "flour"], "Chocolate cake", "dessert")
    cookbook.add_recipe(recipe)
    print(str(recipe))
    cookbook.get_recipe_by_name("Omelette")
    lunches = cookbook.get_recipes_by_types("lunch")
    print(lunches)


if __name__ == "__main__":
    main()
