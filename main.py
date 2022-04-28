#!/usr/bin/env python3

from elevator import Elevator, DumbElevator, SmartElevator


def print_state(state: Elevator) -> None:
    print(f"Current floor: {state.curr_floor}")
    print(f"Direction: {state.direction}")


def evaluate_changes(state: Elevator, changes: str) -> Elevator:
    if changes == "next":
        state.next()
    elif changes.split()[0] == "call":
        desired_floor = int(changes.split()[1])
        state.called_floor(desired_floor)
    elif changes.split()[0] == "press":
        desired_floor = int(changes.split()[1])
        state.pressed_floor(desired_floor)
    return state


def read_changes() -> str:
    line = input("> ")
    return line


if __name__ == "__main__":
    elevator_type = 1
    if elevator_type == 1:
        state = DumbElevator()
    else:
        state = SmartElevator()
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
