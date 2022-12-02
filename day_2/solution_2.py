shape_to_points = {
    'A': 1,
    'B': 2,
    'C': 3
}

game_to_points = {
    'X': 0,
    'Y': 3,
    'Z': 6
}

game_to_shape = {
    'AX': 'C',
    'AY': 'A',
    'AZ': 'B',
    'BX': 'A',
    'BY': 'B',
    'BZ': 'C',
    'CX': 'B',
    'CY': 'C',
    'CZ': 'A'
}

points = 0

with open('input', 'r') as f:
    while line := f.readline():
        line = line.replace(' ', '').replace('\n', '')
        shape = game_to_shape[line]
        points += shape_to_points[shape] + game_to_points[line[-1]]

print(f'My total score would be {points} points.')
