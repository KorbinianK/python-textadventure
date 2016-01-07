import textwrap, random

with open('name.txt', 'r') as f:
    names = f.read().splitlines()
    random.shuffle(names)

with open('pre.txt', 'r') as f:
    pre = f.read().splitlines()

with open('adjective.txt', 'r') as f:
    adjectives = f.read().splitlines()
    random.shuffle(adjectives)

with open('type.txt', 'r') as f:
    types = f.read().splitlines()
    random.shuffle(types)

with open('objective.txt', 'r') as f:
    objectives = f.read().splitlines()
    random.shuffle(objectives)

combined = zip(names,pre,adjectives,types,objectives)
abc = random.shuffle(combined)

print ' '.join(combined[1])
