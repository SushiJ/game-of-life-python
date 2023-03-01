import random
import sys

WIDTH = 5
HEIGHT = 5


def dead_state(w, h):
    state = []

    for _ in range(h):
        inner_list = []
        for _ in range(w):
            inner_list.append(0)

        state.append(inner_list)
    return state


def random_state(w, h):
    state = dead_state(w, h)

    for row in state:
        for i in range(len(row)):
            row[i] = round(random.random())
    return state


def render(state):
    for row in state:
        sys.stdout.write('|')
        for char in row:
            if char == 0:
                sys.stdout.write('#')
            if char == 1:
                sys.stdout.write(' ')
        sys.stdout.write('|')
        sys.stdout.write('\n')


if __name__ == "__main__":
    render(random_state(10, 5))
