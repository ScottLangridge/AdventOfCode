import math
import random
from itertools import combinations


class Ingredient:
    next_id = 0

    def __init__(self, name, capacity, durability, flavor, texture, calories):
        self.id = Ingredient.next_id
        self.name = name
        self.capacity = capacity
        self.durability = durability
        self.flavor = flavor
        self.texture = texture
        self.calories = calories
        Ingredient.next_id += 1


def main(raw_input):
    ingredients = [parse_ingredient(x) for x in raw_input.splitlines()]
    recipes_possible = get_recipes(ingredients, 100)
    recipe_scores = [score(x) for x in recipes_possible]
    recipes_500_cal = filter(lambda x: x[1] == 500, recipe_scores)

    return max([x[0] for x in recipes_500_cal])


def get_recipes(ingredients, ingredient_spaces):
    if ingredient_spaces == 0:
        return [dict()]
    elif len(ingredients) == 1:
        return [{ingredients[0]: ingredient_spaces}]

    current_ingredient = ingredients[0]
    recipes = []
    for i in range(ingredient_spaces + 1):
        new_recipe_base = {current_ingredient: i}
        recipe_completion_options = get_recipes(ingredients[1:], ingredient_spaces - i)
        recipes.extend([new_recipe_base | completion for completion in recipe_completion_options])
    return recipes


def score(cookie):
    capacity, durability, flavor, texture, calories = 0, 0, 0, 0, 0
    for ingredient, quantity in cookie.items():
        capacity += quantity * ingredient.capacity
        durability += quantity * ingredient.durability
        flavor += quantity * ingredient.flavor
        texture += quantity * ingredient.texture
        calories += quantity * ingredient.calories

    if min([capacity, durability, flavor, texture]) < 0:
        return 0, calories
    else:
        return capacity * durability * flavor * texture, calories


def parse_ingredient(string):
    tokens = string.split()
    return Ingredient(
        tokens[0].strip(':'),
        int(tokens[2].strip(',')),
        int(tokens[4].strip(',')),
        int(tokens[6].strip(',')),
        int(tokens[8].strip(',')),
        int(tokens[10].strip(','))
    )


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
