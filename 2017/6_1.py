reg_str = "11	11	13	7	0	15	5	5	4	4	1	1	7	1	15	11"

# 16 registers
regs = [int(s) for s in reg_str.split()]

max_idx = lambda L: L.index(max(L))
seen = set()

cycles = 0
special = [1, 0, 14, 14, 12, 12, 10, 10, 8, 8, 6, 6, 4, 3, 2, 1]
while tuple(regs) not in seen:
    if tuple(special) == tuple(regs):
        cycles = 0
    seen.add(tuple(regs))
    m = max(regs)
    max_idx = regs.index(m)
    regs[max_idx] = 0
    for i in range(1, m + 1):
        regs[(max_idx + i) % len(regs)] += 1
    cycles += 1

print(cycles, regs)
