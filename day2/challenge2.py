import re

from functools import reduce  # Required in Python 3
import operator
def prod(iterable):
    return reduce(operator.mul, iterable, 1)

def main():
    file_name = 'input.txt'
    lines = open(file_name, "r")

    products = []
    for line in lines:

        game = line.strip()  # remove \n from the end of the string
        game_nr_and_cubes = game.split(": ")
        rounds = game_nr_and_cubes[1].split("; ")
        max_val = {'red':-1, 'blue':-1, 'green':-1}  #store maximum of each line in a dictionary

        for round in rounds:
            extracted_values = round.split(', ')
            for single_value_string in extracted_values:
                nr_cubes = int(single_value_string.split(' ')[0])
                colour = single_value_string.split(' ')[1]
                if nr_cubes > max_val[colour]:
                    max_val[colour] = nr_cubes

        val = prod(cube_value for cube_value in max_val.values() if cube_value != -1)
        products.append(val)

    print(sum(products))

main()
