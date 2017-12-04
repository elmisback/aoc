def neighbor_sum(p_x, p_y, d):
    neighbors = [
        (1, 1),
        (-1, 1),
        (1, -1),
        (1, 0),
        (0, 1),
        (-1, -1),
        (-1, 0),
        (0, -1),
            ]
    return sum(d.get((p_x + dx, p_y + dy), 0) for (dx, dy) in neighbors)

def spiral(inp):
    inp = inp
    i = 0
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    p_x, p_y = (0, 0)
    side_length = 0
    a = dict()
    a[(0, 0)] = 1
    while side_length < inp:
        for side, d in enumerate(directions):
            if side % 2 == 0: side_length += 1
            for s in range(side_length):
                p_x += d[0]
                p_y += d[1]
                print(a)
                print(a.get((-1, 1), None))
                a[(p_x, p_y)] = neighbor_sum(p_x, p_y, a)
                if a[(p_x, p_y)] > inp:
                    print(a[(p_x, p_y)])
                    return

spiral(1)
spiral(2)
spiral(3)
spiral(4)
spiral(5)
spiral(1024)
spiral(368078)
