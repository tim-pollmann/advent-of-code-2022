items = '_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
sum = 0

with open('input', 'r') as f:
    while line := f.readline():
        group = [
            set(line.replace('\n', '')),
            set(f.readline().replace('\n', '')),
            set(f.readline().replace('\n', ''))
        ]
        common_item = list(set.intersection(*group))[0]
        sum += items.rindex(common_item)

print(f'The sum of the priorities {sum}.')
