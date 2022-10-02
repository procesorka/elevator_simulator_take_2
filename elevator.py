class Elevator:
    def __init__(self, min_floor=0, max_floor=5):
        if max_floor <= min_floor:
            raise Exception("Top floor must be greater than the lowest one.")
        self.type = None
        self.min_floor = min_floor
        self.max_floor = max_floor
        self.occupancy = False
        self.direction = 0
        self.curr_floor = 0

    def all_floors(self) -> range:
        return range(self.min_floor, self.max_floor + 1)

    def is_valid_floor(self, floor: int) -> bool:
        return floor in self.all_floors()

    def next(self):
        pass

    def called_floor(self, floor_called: int, direction_called: {-1, 0, 1}) -> bool:
        pass

    def pressed_floor(self, floor_pressed: int) -> bool:
        pass

    def display(self):
        pass

    def people_in(self):
        pass

    def people_out(self):
        pass


class DumbElevator(Elevator):
    def __init__(self, min_floor=0, max_floor=5):
        super().__init__(min_floor, max_floor)
        self.type = "Dumb elevator"
        self.destination_floor = 0

    def display(self) -> str:
        available = self.direction == 0 and self.occupancy is False
        return f"Floor: {self.curr_floor}\nAvailable: {available}"

    def next(self) -> bool:
        if self.destination_floor != self.curr_floor:
            self.curr_floor += self.direction
            return True
        self.direction = 0
        return False

    def called_floor(self, floor_called: int, direction_called=0) -> bool:
        if self.direction == 0 and self.occupancy is False and floor_called != self.curr_floor:
            self.destination_floor = floor_called
            self.direction = 1 if self.destination_floor > self.curr_floor else -1
            return True
        return False

    def pressed_floor(self, floor_pressed: int) -> bool:
        if self.direction == 0 and self.occupancy is True and floor_pressed != self.curr_floor:
            self.destination_floor = floor_pressed
            self.direction = 1 if self.destination_floor > self.curr_floor else -1
            return True
        return False

    def people_in(self):
        if self.direction == 0:
            self.occupancy = True

    def people_out(self):
        if self.direction == 0:
            self.occupancy = False


class SmartElevator(Elevator):
    def __init__(self, min_floor=0, max_floor=5):
        super().__init__(min_floor, max_floor)
        self.type = "Smart elevator"
        self.general_direction = 1
        self.floors_to_visit = [0]*(self.max_floor - self.min_floor + 1)

    def display(self):
        return f"Floor: {self.curr_floor}\nDirection: {self.direction}\n" \
               f"General direction: {self.general_direction}\nOccupancy: {self.occupancy}\n{self.floors_to_visit}"

    def next(self):
        if (self.curr_floor == self.max_floor and self.general_direction == 1) or \
                (self.curr_floor == self.min_floor and self.general_direction == -1):
            self.general_direction *= -1

        self.direction = self.general_direction

        if self.floors_to_visit[self.curr_floor - self.min_floor] != 0:
            self.floors_to_visit[self.curr_floor - self.min_floor] = 0
            self.direction = 0
        else:
            self.curr_floor += self.direction

    def called_floor(self, floor_called: int, direction_called: {-1, 1}) -> bool:
        if floor_called == self.curr_floor and direction_called == self.general_direction:
            return False
        self.floors_to_visit[floor_called - self.min_floor] = direction_called
        if not any(self.floors_to_visit):
            self.direction = self.general_direction = direction_called
        return True

    def pressed_floor(self, floor_pressed: int) -> bool:
        if self.occupancy is True and floor_pressed != self.curr_floor:
            future_direction = 1 if floor_pressed > self.curr_floor else -1
            print(future_direction)
            self.floors_to_visit[floor_pressed - self.min_floor] = future_direction
            return True
        return False

    def people_in(self):
        if self.direction == 0:
            self.occupancy = True

    def people_out(self):
        if self.direction == 0:
            self.occupancy = False
    