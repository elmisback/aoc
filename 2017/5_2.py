with open('5.txt') as f:
    values = [int(v) for v in f.readlines()]

pos = 0
steps = 0
while pos >= 0 and pos < len(values):
    last = pos
    pos += values[pos]
    values[last] += -1 if values[last] >= 3 else 1
    steps += 1

print(steps)
