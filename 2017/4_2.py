with open('4.txt', 'r') as f:
    phrases = [[frozenset(w) for w in line.split()] for line in f.readlines()]

print(sum([1 for p in phrases if len(set(p)) == len(p)]))
