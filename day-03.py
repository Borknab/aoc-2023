ans = 0

with open('input-03.txt') as f:
    line_idx = 1
    lines = f.readlines()
    visited = set()
    numbers = []
    lines = [line.strip() for line in lines]
    gear_ratios = []

    for y in range(len(lines)):
        for x in range(len(lines[0])):
            cur_el = lines[y][x]
            cur_numbers = []
            if not cur_el.isnumeric() and cur_el != '.':
                neighbors = [[y - 1, x], [y - 1, x - 1], [y - 1, x + 1], [y, x - 1], [y, x + 1], [y + 1, x], [y + 1, x - 1], [y + 1, x + 1]]
                for n in neighbors:
                    if 0 <= n[0] < len(lines) and 0 <= n[1] < len(lines[0]) and lines[n[0]][n[1]].isnumeric():
                        left = n[1]
                        right = n[1]
                        while left - 1 >= 0 and lines[n[0]][left - 1].isnumeric(): left -= 1
                        while right + 1 < len(lines[0]) and lines[n[0]][right + 1].isnumeric(): right += 1
                        number = lines[n[0]][left : right + 1]
                        if (n[0], left) not in visited: 
                            numbers.append(number)
                            cur_numbers.append(number)
                        visited.add((n[0], left))
            if len(cur_numbers) == 2 and cur_el == "*":
                gear_ratios.append(int(cur_numbers[0]) * int(cur_numbers[1]))
    
    # Part 1
    numbers = [int(n) for n in numbers]
    print(sum(numbers))

    # Part 2
    print(sum(gear_ratios))

