n = 0

with open('input', 'r') as f:
    while line := f.readline():
        line = line.replace('\n', '')

print(f'One range fully contains the other in {n} assignment pairs.')
