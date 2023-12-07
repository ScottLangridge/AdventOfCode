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
    hands = 


    # Solve problem

    # Return solution
    return None

def get_hand_score(cards):
    # Scores are integers of the form 01122334455
  
    score = 0
    score += get_hand_score(cards) * 10000000000
  
  

def get_hand_type(cards):
    counts = sorted(Counted(cards).values())
    if counts = [1, 1, 1, 1, 1]:
        return 1
    if counts = [2, 1, 1, 1]:
        return 2
    if counts = [2, 2, 1]:
        return 3
    if counts = [3, 1, 1]:
        return 4
    if counts = [3, 2]:
        return 5
    if counts = [4, 1]:
        return 6
    if counts = [5]:
        return 7
    

def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
