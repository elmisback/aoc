states = dict()

def parse_state(lines):
    state_name = lines[0].split()[-1][0]
    v_0 = int(lines[2].split()[-1][0])
    v_1 = int(lines[6].split()[-1][0])
    m_0 = 1 if lines[3].split()[-1] == 'right.' else -1
    m_1 = 1 if lines[7].split()[-1] == 'right.' else -1
    c_0 = lines[4].split()[-1][0]
    c_1 = lines[8].split()[-1][0]
    states[state_name] = lambda v: (v_1, m_1, c_1) if v else (v_0, m_0, c_0)

def parse(fname):
    with open(fname, 'r') as f:
        states = f.read().split('\n\n')
    for state in states:
        parse_state(state.splitlines())

steps = 12523873
parse('25.txt')

def update(state, loc, L):
    tup = states[state](L[loc])
    L[loc] = tup[0]
    loc += tup[1]
    if loc < 0:
        L = [0] + L
        loc = 0
    elif loc == len(L):
        L = L + [0]
    state = tup[2]
    return (state, loc, L)

step = 0
state = 'A'
loc = 0
L = [0]

while step < steps:
    (state, loc, L) = update(state, loc, L)
    step += 1
    if not step % 10000: print(step)

print(sum(L))
