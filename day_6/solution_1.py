with open('input', 'r') as f:
    code = f.readline()

i = 3
while len(set([code[i - j] for j in range(4)])) != 4:
    i += 1

print(f'The start-of-packet marker is {i + 1}.')
