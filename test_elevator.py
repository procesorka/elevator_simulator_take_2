from elevator import DumbElevator
import unittest


class DumbElevatorTests(unittest.TestCase):
    @staticmethod
    def test_movement():
        state = DumbElevator()
        state.people_in()
        state.pressed_floor(3)
        assert(state.curr_floor == 0)
        state.next()
        assert(state.curr_floor == 1)
        state.next()
        assert(state.curr_floor == 2)
        state.next()
        assert(state.curr_floor == 3)
        state.next()
        assert(state.curr_floor == 3)

    @staticmethod
    def test_occupancy():
        state = DumbElevator()
        state.pressed_floor(1)
        state.next()
        assert(state.curr_floor == 0)

        state.people_in()
        state.pressed_floor(1)
        state.next()
        assert(state.curr_floor == 1)


if __name__ == "__main__":
    unittest.main()