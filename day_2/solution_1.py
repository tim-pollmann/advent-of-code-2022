shape_to_points = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

game_to_points = {
    'AZ': 0,
    'BX': 0,
    'CY': 0,
    'AX': 3,
    'BY': 3,
    'CZ': 3,
    'AY': 6,
    'BZ': 6,
    'CX': 6
}

points = 0

with open('input', 'r') as f:
    while line := f.readline():
        line = line.replace(' ', '').replace('\n', '')
        points += shape_to_points[line[-1]] + game_to_points[line]

print(f'My total score would be {points} points.')
