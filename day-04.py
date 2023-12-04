from collections import defaultdict

ans = 0
with open('input-04.txt') as f:
    card_idx = 1
    copied = defaultdict(int)
    num_copied = 0

    for line in f:
        if card_idx not in copied: copied[card_idx] = 0
        win_numbers, my_numbers = line.split(":")[1].split("|")
        win_numbers, my_numbers = win_numbers.strip(), my_numbers.strip()
        win_numbers = set([int(x) for x in win_numbers.split(" ") if x.isnumeric()])
        my_numbers = [int(x) for x in my_numbers.split(" ") if x.isnumeric()]
        copy_idx = card_idx + 1
        copy_indices = []
        for n in my_numbers:
            if n in win_numbers:
                copy_indices.append(copy_idx)
                copy_idx += 1
        if copied[card_idx] > 0: 
            copy_indices = copy_indices * (copied[card_idx] + 1)
        for c in copy_indices:
            copied[c] += 1
            num_copied += 1
        card_idx += 1

    # Part 2
    print(card_idx + num_copied - 1)