import time
from collections import defaultdict


def main():
    # print('Test:', solve(get_input('example.txt')), '\n')
    print('Solution:', solve(get_input()))
    pass


def get_input(filepath='input.txt'):
    out = []
    with open(filepath, 'r') as f:
        raw = f.readlines()

    for line in raw:
        out.append(line.strip('\n'))
    return out


def solve(puzzle_input):
    inch_claimed_by = {}
    claims_with_no_overlap = []
    overlaps = 0
    for claim in puzzle_input:
        claim_overlaps = False
        for inch in get_claim_inches(claim):
            if inch not in inch_claimed_by.keys():
                inch_claimed_by[inch] = [get_id(claim)]
            else:
                if len(inch_claimed_by[inch]) == 1:
                    if inch_claimed_by[inch][0] in claims_with_no_overlap:
                        claims_with_no_overlap.remove(inch_claimed_by[inch][0])
                    overlaps += 1
                inch_claimed_by[inch].append(get_id(claim))
                claim_overlaps = True
        if not claim_overlaps:
            claims_with_no_overlap.append(get_id(claim))

    return overlaps


def get_claim_inches(claim):
    split_claim = claim.split(' ')
    x = x_margin = int(split_claim[2].split(',')[0])
    y = y_margin = int(split_claim[2].split(',')[1][:-1])
    width = int(split_claim[3].split('x')[0])
    height = int(split_claim[3].split('x')[1])

    claimed = []
    for y in range(y_margin, y_margin + height):
        for x in range(x_margin, x_margin + width):
            claimed.append(str(x) + ',' + str(y))

    return claimed


def get_id(claim):
    return claim.split(' ')[0][1:]


start_time = time.time()
main()
end_time = time.time()
print('\n' + ''.join(['-'] * 26) + '\nFINISHED\nTIME:', end_time - start_time,
      '\n' + ''.join(['-'] * 26))
input()
