with open('4.txt', 'r') as f:
    phrases = [line.split() for line in f.readlines()]

print(len([p for p in phrases if len(set(p)) == len(p)]))
