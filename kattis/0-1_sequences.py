# https://open.kattis.com/problems/sequences

import random
import time


def create_sequence():
    sequence = []
    content = ['0', '1', '?']
    for n in range(random.randint(1, 100)):
        sequence.append(random.choice(content))

    return sequence


def new_sequence(sequence):
    content = ['0', '1']

    for n in range(0, len(sequence)):
        if sequence[n] == '?':
            sequence[n] = content[random.randint(0, 1)]

    return sequence


def sort(sequence):
    times = 0
    start = time.time()
    for n in range(10000):
        for n in range(0, len(sequence) - 1):
            if sequence[n] == '1' and sequence[n + 1] == '0':
                for n in range(0, len(sequence) - 1):
                    if sequence[n] == '1' and sequence[n + 1] == '0':
                        sequence[n + 1] = '1'
                        sequence[n] = '0'

                        times += 1
                        print(f'Sorted sequence: {sequence}')

    print(
        f'\nThe length of the sequence was {len(sequence)}, it ran the sort function {times} times and took {time.time() - start:.2f} seconds to execute.')


def main():
    sequence = create_sequence()
    print(f'Original sequence: {sequence}')
    recreated_sequence = new_sequence(sequence)
    print(f'Recreated sequence: {recreated_sequence}\n')

    sort(recreated_sequence)


if __name__ == '__main__':
    main()
