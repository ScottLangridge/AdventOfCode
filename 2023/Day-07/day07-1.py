from collections import Counter


CARD_SCORES = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14,
} 


def main(raw_input):
    hands = [hand.split() for hand in raw_input.splitlines()]
    ranked_hands = sorted(hands, key=lambda i: get_hand_score(i[0]))

    total_winnings = 0
    for i, hand in enumerate(ranked_hands):
        total_winnings += (i + 1) * int(hand[1])

    return total_winnings


# Scores are integers of the form 01122334455. The first digit is the type score, the rest are the cards.
def get_hand_score(cards):
    score = 0
    score += get_hand_type(cards) * 10000000000
    score += CARD_SCORES[cards[0]] * 100000000
    score += CARD_SCORES[cards[1]] * 1000000
    score += CARD_SCORES[cards[2]] * 10000
    score += CARD_SCORES[cards[3]] * 100
    score += CARD_SCORES[cards[4]] * 1
    return score


def get_hand_type(cards):
    counts = sorted(Counter(cards).values(), reverse=True)
    if counts == [1, 1, 1, 1, 1]:
        return 1
    if counts == [2, 1, 1, 1]:
        return 2
    if counts == [2, 2, 1]:
        return 3
    if counts == [3, 1, 1]:
        return 4
    if counts == [3, 2]:
        return 5
    if counts == [4, 1]:
        return 6
    if counts == [5]:
        return 7
    raise 'Should not get here'
    

def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
