from functools import partial

blocks = []
for block in iter(input, 'done'):
    blocks.append(block)

print(blocks)