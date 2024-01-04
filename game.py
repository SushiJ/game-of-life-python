import random

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
        print('|', end="")
        for char in row:
            if char == 0:
                print("#", end="")
            else:
                print(" ", end="")
        print('|')


if __name__ == "__main__":
    render(random_state(10, 5))
