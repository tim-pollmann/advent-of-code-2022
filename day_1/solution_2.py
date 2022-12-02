current = 0
calories = []

with open('input', 'r') as f:
    while line := f.readline():
        if line == '\n':
            calories.append(current)
            current = 0
            continue

        current += int(line)

third_most = sum(sorted(calories, reverse=True)[:3])
print(f'The elfs with third most calories are carrying {third_most} calories.')
