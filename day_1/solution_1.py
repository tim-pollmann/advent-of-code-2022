current = 0
max = 0

with open('input', 'r') as f:
    while line := f.readline():
        if line == '\n':
            if current > max:
                max = current
            current = 0
            continue

        current += int(line)

print(f'The elf with most calories is carrying {max} calories.')
