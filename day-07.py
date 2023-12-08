from collections import Counter
from functools import cmp_to_key
from itertools import product

strenghts = {
    "A": 13, 
    "K": 12,
    "Q": 11,
    "T": 10,
    "9": 9, 
    "8": 8,
    "7": 7,
    "6": 6, 
    "5": 5, 
    "4": 4, 
    "3": 3,
    "2": 2,
    "J": 1
}

def cmp_hands(hand1, hand2):
    for i in range(5):
        l1s = strenghts[hand1[i]]
        l2s = strenghts[hand2[i]]
        if l1s == l2s: continue
        elif l1s > l2s: return -1
        else: return 1
    return 0

def combo_power(hand):
    hand_options = []
    if "J" in hand:
        j_clones = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
        num_j = Counter(hand)["J"]
        pos_js = product(j_clones, repeat=num_j)
        for pos_j in pos_js:
            new_hand = []
            jp = 0
            for h in hand:
                if h == "J":
                    new_hand.append(pos_j[jp])
                    jp += 1
                else:
                    new_hand.append(h)
            hand_options.append("".join(new_hand))
    else:
        hand_options.append(hand)

    possible_powers = []
    for opt in hand_options:
        hand = opt
        cnt = Counter(hand)
        max_cards = max(cnt.values())

        p = [0]
        if max_cards == 5: p[0] = 7
        elif max_cards == 4: p[0] = 6
        elif max_cards == 3 and len(cnt) == 2: p[0] = 5
        elif max_cards == 3: p[0] = 4
        elif list(sorted(cnt.values())) == [1,2,2]: p[0] = 3
        elif max_cards == 2: p[0] = 2
        else: p[0] = 1

        possible_powers.append(p[0])

    return max(possible_powers)

ans = 0
with open('input-07.txt') as f:
    hands, bids = [], []
    for line in f:
        hand, bid = line.split(" ")[0], line.split(" ")[1]
        hands.append(hand)
        bids.append(int(bid))
    bid_map = {}
    for h in range(len(hands)):
        bid_map[hands[h]] = bids[h]
    results = {}
    for i in range(1, 8): results[i] = []
    for h in hands: results[combo_power(h)].append(h)
    
    for r in results:
        new_res = sorted(results[r], key=cmp_to_key(cmp_hands))
        results[r] = new_res
    
    ranks = []
    for i in range(7, 0, -1):
        ranks.extend(results[i])
    
    rank = len(hands)
    for r in ranks:
        bid = bid_map[r]
        ans += bid * rank
        rank -= 1

print(ans)