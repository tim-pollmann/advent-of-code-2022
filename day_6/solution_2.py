with open('input', 'r') as f:
    code = f.readline()

i = 14
while len(set([code[i - j] for j in range(14)])) != 14:
    i += 1

print(f'The start-of-message marker is {i + 1}.')
