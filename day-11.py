from collections import deque

with open('input-11.txt') as f:
    lines = [l.strip() for l in f.readlines()]
    space = []
    for y in range(len(lines)):
        space_row = []
        for x in range(len(lines[0])):
            space_row.append([y,x])
        space.append(space_row)
                
    # STEP 1: Expand space
    i = 0
    rows = []
    for i in range(len(lines)):
        l = lines[i]
        if all([x == "." for x in l]):
            rows.append(i)
    for r in range(len(space)):
        if r in rows:
            for i in range(r, len(space)):
                for j in range(len(space[0])):
                    space[i][j][0] += 999_999

    cols = []
    for x in range(len(lines[0])):
        all_dots = True
        for y in range(len(lines)):
            if lines[y][x] != ".":
                all_dots = False
                break
        if all_dots:
            cols.append(x)
    for c in range(len(space[0])):
        if c in cols:
            for x in range(c, len(space[0])):
                for y in range(len(space)):
                    space[y][x][1] += 999_999

    # STEP 2: Compute distances
    galaxies = []
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if lines[y][x] == "#":
                galaxies.append(space[y][x])
    pairs = []
    for i in range(len(galaxies) - 1):
        for j in range(i + 1, len(galaxies)):
            pairs.append([galaxies[i], galaxies[j]])

    sum_dist = 0
    for v1, v2 in pairs:
        sum_dist += abs(v1[0] - v2[0]) + abs(v1[1] - v2[1])

    print(sum_dist)