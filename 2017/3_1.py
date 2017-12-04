def spiral(step):
    step = step - 1
    i = 0
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    p_x, p_y = (0, 0)
    side_length = 0
    while i < step:
        for side, d in enumerate(directions):
            if side % 2 == 0: side_length += 1
            p_x += d[0] * side_length
            p_y += d[1] * side_length
            i += side_length
            if i > step:
                p_x -= d[0] * (i - step)
                p_y -= d[1] * (i - step)
                break

    print(abs(p_x) + abs(p_y))

spiral(1)
spiral(12)
spiral(23)
spiral(1024)
spiral(368078)
