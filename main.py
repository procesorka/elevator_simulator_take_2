#!/usr/bin/env python3

class Elevator:
    pass


def print_state(state):
    pass


def evaluate_changes(state, changes):
    return state


def read_changes():
    return ()


if __name__ == "__main__":
    state = Elevator()
    print_state(state)

    # This is an:
    while True:
        # Read
        changes = read_changes()
        # Eval
        state = evaluate_changes(state, changes)
        # Print
        print_state(state)
        # Loop—a REPL!
