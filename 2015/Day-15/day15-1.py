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
    possible_swaps = [(x[0], x[1]) for x in list(combinations(ingredients, 2))]
    possible_swaps.extend([tuple(reversed(x)) for x in possible_swaps])

    cookie = {}
    for i in ingredients:
        cookie[i] = 0
    for _ in range(100):
        cookie[random.choice(ingredients)] += 1

    temp = 50000
    stop_temp = 0.001
    cooling_coeff = 0.9999
    i = 0
    while temp * (cooling_coeff ** i) > stop_temp:
        cookie = step_once(cookie, possible_swaps, temp * (cooling_coeff ** i))
        i += 1

    return fitness(cookie)


def step_once(cookie, possible_swaps, temp):
    current_score = fitness(cookie)
    random.shuffle(possible_swaps)
    for swap in possible_swaps:
        new_score = fitness_after_swap(cookie, swap)
        accept_probability = math.e ** ((new_score - current_score) / temp)
        if random.uniform(0, 1) <= accept_probability:
            apply_swap(cookie, swap)
            return cookie
    return cookie


def fitness_after_swap(cookie, swap):
    apply_swap(cookie, swap)
    out = fitness(cookie)
    revert_swap(cookie, swap)
    return out


def fitness(cookie):
    capacity, durability, flavor, texture = 0, 0, 0, 0
    for ingredient, quantity in cookie.items():
        capacity += quantity * ingredient.capacity
        durability += quantity * ingredient.durability
        flavor += quantity * ingredient.flavor
        texture += quantity * ingredient.texture

    if min([capacity, durability, flavor, texture]) < 0:
        return 0
    else:
        return capacity * durability * flavor * texture


def apply_swap(cookie, swap):
    cookie[swap[0]] -= 1
    cookie[swap[1]] += 1


def revert_swap(cookie, swap):
    cookie[swap[0]] += 1
    cookie[swap[1]] -= 1


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
