n = 0

with open('input', 'r') as f:
    while line := f.readline():
        range_1, range_2 = line.replace('\n', '').split(',')
        
        lower_1, upper_1 = range_1.split('-')
        lower_2, upper_2 = range_2.split('-')

        set_1 = set(range(int(lower_1), int(upper_1) + 1))
        set_2 = set(range(int(lower_2), int(upper_2) + 1))
        
        if set_1 <= set_2 or set_1 >= set_2:
            n += 1

print(f'One range fully contains the other in {n} assignment pairs.')
