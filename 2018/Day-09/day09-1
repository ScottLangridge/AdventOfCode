import time


def main():
    # print('Test:', solve(get_input('example1.txt')),'\n')
    print('Solution:', solve(get_input()))
    pass


def get_input(filepath='input.txt'):
    with open(filepath, 'r') as f:
        raw = f.readlines()
    
    raw = raw[0].split(' ')
    players = int(raw[0])
    marbles = int(raw[-2])

    return players, marbles


def solve(puzzle_input):
    players = [0]*puzzle_input[0]
    marbles = [0, 1]

    current_marble = 1
    current_player = 1
    for i in range(2, puzzle_input[1] + 1):
        if i % 23 != 0:
            current_marble = (current_marble + 2) % len(marbles)
            marbles.insert(current_marble, i)
        else: 
            players[current_player] += i
            current_marble = current_marble - 7
            if current_marble < 0:
                current_marble = len(marbles) + current_marble
            players[current_player] += marbles[current_marble]
            del marbles[current_marble]

        current_player += 1
        if current_player == len(players):
            current_player = 0
    
    return max(players)

start_time = time.time()
main()
end_time = time.time()
print('\n' + ''.join(['-'] * 26) + '\nFINISHED\nTIME:', end_time - start_time,
      '\n' + ''.join(['-'] * 26))
input()
