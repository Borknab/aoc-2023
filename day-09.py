
with open('input-09.txt') as f:
    lines = [[int(x) for x in l.strip().split(" ")] for l in f.readlines()]
    for l in lines:
        l.reverse()
    ans = 0
    for seq in lines:
        diff = [seq]
        while True:
            cur_diff = diff[-1]
            new_diff = []
            for i in range(len(cur_diff) - 1):
                new_diff.append(cur_diff[i + 1] - cur_diff[i])
            diff.append(new_diff)
            if all([x == new_diff[0] == 0 for x in new_diff]): break
        print(diff)
        print()
        seq_res = 0
        for d in diff:
            seq_res += d[-1]
        ans += seq_res
    
    print(ans)
        