from collections import deque

# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.

# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.

# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.

# . is ground; there is no pipe in this tile.
# S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.

cnts = {
    "|": {"down" : ["L", "J", "|"], "up": ["7", "F", "|"]},
    "-": {"right": ["7", "J", "-"], "left": ["L", "F", "-"]},
    "L": {"up": ["|", "F", "7"], "right": ["-", "J", "7"]},
    "J": {"up": ["|", "F", "7"], "left": ["-", "F", "L"]},
    "7": {"left": ["-", "F", "L"], "down": ["|", "J", "L"]},
    "F": {"right": ["-", "7", "J"], "down": ["|", "L", "J"]},
    "S": {"up": ["|", "F", "7"], "right": ["7", "-", "J"], "down": ["|", "J", "L"], "left": ["-", "F", "L"]} 
}

def go_in_dir(y, x, d):
    if d == "down": return y + 1, x
    elif d == "up": return y - 1, x
    elif d == "left": return y, x - 1
    elif d == "right": return y, x + 1

with open('input-10.txt') as f:
    maze = []
    row = 0
    start_pos = []
    for line in f:
        for i in range(len(line)):
            c = line[i]
            if c == "S":
                start_pos = [row, i]
        maze.append(line.strip())
        row += 1
    depth_map = [["." for c in line] for line in maze]

    visited = set()
    max_depth = [-1]
    queue = deque([[start_pos[0], start_pos[1], 0]])

    while queue:
        [y, x, depth] = queue.popleft()

        if (y, x) in visited: continue
        if maze[y][x] == "." or y >= len(maze) or y < 0 or x < 0 or x >= len(maze[0]): continue

        visited.add((y, x))
        depth_map[y][x] = "x" 
        if maze[y][x] in cnts:
            max_depth[0] = max(max_depth[0], depth)
            for d in cnts[maze[y][x]]:
                new_y, new_x = go_in_dir(y, x, d)
                if new_y >= len(maze) or new_y < 0 or new_x < 0 or new_x >= len(maze[0]): continue
                if maze[new_y][new_x] in cnts[maze[y][x]][d]:
                    queue.append([new_y, new_x, depth + 1])

    points = []
    for y in range(len(depth_map)):
        for x in range(len(depth_map[0])):
            if depth_map[y][x] == "x":
                ns = [[-1,-1], [-1, 0], [-1, 1], [1, -1], [1, 0], [1, 1], [0, -1], [0, 1]]
                for n in ns:
                    new_y, new_x = y + n[0], x + n[1]
                    if new_y >= 0 and new_x >= 0 and new_y < len(depth_map) and new_x < len(depth_map[0]) and depth_map[new_y][new_x] == ".":
                        depth_map[y][x] = "B"
                        break