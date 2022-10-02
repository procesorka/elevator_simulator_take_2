#!/usr/bin/env python3
import sys

from elevator import Elevator, DumbElevator, SmartElevator


def print_state(state: Elevator) -> None:
    print(state.display())


def evaluate_changes(state: Elevator, changes: str) -> Elevator:
    if changes == "":
        state.next()
    elif changes == "in":
        state.people_in()
    elif changes == "out":
        state.people_out()
    elif " " in changes and len(changes.split()) >= 2:
        try:
            desired_floor = int(changes.split()[1])
        except ValueError:
            print("Floor must be a number!")
        else:
            if state.is_valid_floor(desired_floor):
                if changes.split()[0].lower() == "press":
                    state.pressed_floor(desired_floor)
                elif changes.split()[0].lower() == "call":
                    try:
                        direction_called = int(changes.split()[2])
                    except IndexError:
                        state.called_floor(desired_floor, 1)
                    except ValueError:
                        print("Direction must be 1 for up or -1 for down.")
                    else:
                        if direction_called in {1, -1}:
                            state.called_floor(desired_floor, direction_called)
                        else:
                            print("Direction must be 1 for up or -1 for down.")
            else:
                print(f"The {desired_floor} floor doesn't exist in this building!")
    else:
        print("Unknown command!")
    return state


def read_changes() -> str:
    line = input("> ")
    return line


if __name__ == "__main__":
    if sys.argv[1] == "dumb":
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
