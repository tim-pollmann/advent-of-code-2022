from typing import List
import re


stacks: List[List[str]] = [
    ['S', 'T', 'H', 'F', 'W', 'R'],
    ['S', 'G', 'D', 'Q', 'W'],
    ['B', 'T', 'W'],
    ['D', 'R', 'W', 'T', 'N', 'Q', 'Z', 'J'],
    ['F', 'B', 'H', 'G', 'L', 'V', 'T', 'Z'],
    ['L', 'P', 'T', 'C', 'V', 'B', 'S', 'G'],
    ['Z', 'B', 'R', 'T', 'W', 'G', 'P'],
    ['N', 'G', 'M', 'T', 'C', 'J', 'R'],
    ['L', 'G', 'B', 'W']
]

with open('input', 'r') as f:
    while line := f.readline():
        amount, source_stack, target_stack = [int(i) for i in re.findall(r'\d+', line)]
        stacks[target_stack - 1].extend(stacks[source_stack - 1][:- amount - 1:- 1]) 
        stacks[source_stack - 1] = stacks[source_stack - 1][:- amount]
        
print(f'The code is "{str().join([stack[- 1] for stack in stacks])}".')
