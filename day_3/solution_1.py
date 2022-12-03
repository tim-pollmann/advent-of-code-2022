items = '_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
sum = 0

with open('input', 'r') as f:
    while line := f.readline():
        line = line.replace('\n', '')
        first, second = line[:len(line) // 2], line[-len(line) // 2:]
        common_item = list(set(first) & set(second))[0]
        sum += items.rindex(common_item)

print(f'The sum of the priorities {sum}.')
