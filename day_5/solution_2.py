import re

with open('input', 'r') as f:
    config, operations = [part.splitlines() for part in f.read().split('\n\n')]
    stacks = [[] for _ in range(int(config[-1][-2]))]

    for line in config[-2::-1]:
        for stack_idx in range(len(stacks)):
            if (crate := line[stack_idx * 4 + 1]) != ' ':
                stacks[stack_idx].append(crate)

    for operation in operations:
        amount, source_stack, target_stack = [int(i) for i in re.findall(r'\d+', operation)]
        stacks[target_stack - 1].extend(stacks[source_stack - 1][- amount:]) 
        stacks[source_stack - 1] = stacks[source_stack - 1][:- amount]
        
print(f'The code is "{str().join([stack[- 1] for stack in stacks])}".')
