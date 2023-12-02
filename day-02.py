ans = 0
power_sum = 0
max_amounts = {"red": 12, "green": 13, "blue": 14}

with open('input-02.txt') as f:
    line_idx = 1
    for line in f:
        sp = line.split(":")[1].split(";")
        game_impossible = False
        powers = {"red": 0, "green": 0, "blue": 0}
        cur_power = 1

        for shuffle in sp:
            shows = shuffle.split(",")
            for sh in shows:
                sh = sh.strip()
                amount, color = sh.split(" ")
                powers[color] = max(powers[color], int(amount))
                if int(amount) > max_amounts[color]:
                    game_impossible = True

        if not game_impossible: ans += line_idx
        for c in powers: cur_power *= powers[c]
        power_sum += cur_power
        line_idx += 1

# Part 1
print(ans)

# Part 2
print(power_sum)