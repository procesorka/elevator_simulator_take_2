#!/usr/bin/env python3

class Elevator:
    def __init__(self, min_floor=0, max_floor=5):
        if max_floor <= min_floor:
            raise Exception("Max_floor must be greater then min_floor.")
        self.min_floor = min_floor
        self.max_floor = max_floor
        self.occupancy = False
        self.direction = 0
        self.curr_floor = 0

    def next(self):
        pass

    def called_floor(self, floor: int):
        pass

    def pressed_floor(self, floor: int):
        pass


def print_state(state: Elevator) -> None:
    print(f"Current floor: {state.curr_floor}")
    print(f"Direction: {state.direction}")


def evaluate_changes(state: Elevator, changes: str) -> Elevator:
    if changes == "next":
        state.next()
    elif changes.split()[0] == "call":
        state.called_floor(changes.split()[1])
    elif changes.split()[0] == "press":
        state.pressed_floor(changes.split()[1])
    return state


def read_changes() -> str:
    line = input("> ")
    return line


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
