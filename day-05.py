from collections import defaultdict

ans = 0
with open('input-05.txt') as f:
    lines = [line.strip() for line in f.readlines()]
    seeds = [int(s) for s in lines.pop(0).split(":")[1].strip().split(" ")]
    new_seeds = []
    for i in range(0, len(seeds) - 1, 2):
        new_seeds.extend(list(range(seeds[i], seeds[i] + 100000)))
    seeds = new_seeds
    lines.pop(0)
    lines.append('')
    map_pointers = []
    for l in range(len(lines)):
        if "map" in lines[l]: map_pointers.append(l)
    mappings = defaultdict(list)

    for p in map_pointers:
        l = p + 1
        while lines[l] != '':
            range_info = [int(x) for x in lines[l].split(" ")]
            mappings[lines[p]].append([range_info[0], [range_info[1], range_info[1] + range_info[2]]])
            l += 1

    
    for m in mappings:
        new_seeds = []
        for s in seeds:
            new_value = None
            for rng in mappings[m]:
                if rng[1][0] <= s <= rng[1][1] - 1:
                    idx = s - rng[1][0]
                    new_value = rng[0] + idx
            new_seeds.append(new_value) if new_value else new_seeds.append(s)
        seeds = new_seeds

    print(min(seeds))