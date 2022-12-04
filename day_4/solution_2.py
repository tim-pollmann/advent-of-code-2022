n = 0

with open('input', 'r') as f:
    while line := f.readline():
        (lower1, upper1), (lower2, upper2) = [[int(x) for x in range.split('-')] for range in line.replace('\n', '').split(',')]
        range1 = set(range(lower1, upper1 + 1))
        range2 = set(range(lower2, upper2 + 1))
        
        if range1 & range2:
            n += 1


print(f'The amount of overlaps is {n}.')
