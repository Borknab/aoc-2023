from collections import defaultdict
import math

with open('input-08.txt') as f:
    lines = [l.strip() for l in f.readlines()]
    instructions = lines[0].strip()
    lines = lines[2:]
    graph = defaultdict(list)
    for l in lines:
        start, dests = [x for x in l.split("=")]
        start = start.strip()
        dests = dests.strip()
        dests = [x.strip() for x in dests[1:-1].split(",")]
        graph[start].extend(dests)

    min_steps = [float("inf")]
    cur_nodes = [x for x in graph if x.endswith("A")]
    n = len(instructions)
    step, mod_step = 0, 0

    visited = {}
    while True:
        break_free = False
        for x in cur_nodes:
            if x.endswith("Z") and not x in visited:
                visited[x] = step
            if len(visited) == len(cur_nodes):
                break_free = True
        if break_free: break

        instr = instructions[mod_step]
        new_cur_nodes = []
        if instr == "L": 
            for curn in cur_nodes: new_cur_nodes.append(graph[curn][0])
        else: 
            for curn in cur_nodes: new_cur_nodes.append(graph[curn][1])
        cur_nodes = new_cur_nodes
        step += 1
        mod_step = step % n

    visited = list(visited.values())
    print(math.lcm(visited[0], visited[1], visited[2], visited[3], visited[4], visited[5]))