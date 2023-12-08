ans = 1

with open('input-06.txt') as f:
    lines = [s.strip() for s in f.readlines()]
    times = [int(x) for x in lines[0].split(":")[1].strip().split(" ") if x.isnumeric()]
    distances = [int(x) for x in lines[1].split(":")[1].strip().split(" ") if x.isnumeric()]

    for t in range(len(times)):
        dist = distances[t]
        time = times[t]
        beaten = 0
        for i in range(time + 1):
            cur_dist = (time - i) * i
            if cur_dist > dist:
                beaten += 1
        ans *= beaten

print(ans)