import re

def main():
    file_name = 'input.txt'
    lines = open(file_name, "r")

    sum_games = 0
    allowed_cubes = {'red': 12, 'green': 13, 'blue': 14}

    for line in lines:
        valid_game = True
        game = line.strip()  # remove \n from the end of the string
        game_nr_and_cubes = game.split(": ")
        game_nr = int(game_nr_and_cubes[0].split(" ")[1])
        rounds = game_nr_and_cubes[1].split("; ")
        for round in rounds:
            extracted_values = round.split(', ')
            for single_value_string in extracted_values:
                nr_cubes = int(single_value_string.split(' ')[0])
                colour = single_value_string.split(' ')[1]
                if nr_cubes > allowed_cubes[colour]:
                    valid_game = False
        if valid_game:
            sum_games += game_nr

    print(sum_games)


main()
