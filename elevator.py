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

    def called_floor(self, floor_called: int):
        pass

    def pressed_floor(self, floor_pressed: int):
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

    def called_floor(self, floor_called: int) -> bool:
        if self.is_valid_floor(floor_called):
            if self.direction == 0 and self.occupancy is False and floor_called != self.curr_floor:
                self.destination_floor = floor_called
                self.direction = 1 if self.destination_floor > self.curr_floor else -1
                return True
            return False
        print(f"The {floor_called} floor doesn't exist in this building!")
        return False

    def pressed_floor(self, floor_pressed: int) -> bool:
        if self.is_valid_floor(floor_pressed):
            if self.direction == 0 and self.occupancy is True and floor_pressed != self.curr_floor:
                self.destination_floor = floor_pressed
                self.direction = 1 if self.destination_floor > self.curr_floor else -1
                return True
            return False
        print(f"The {floor_pressed} floor doesn't exist in this building!")
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
        self.direction = 0
        self.general_direction = 1
        self.floors_to_visit = [0]*(self.max_floor - self.min_floor)

    def display(self):
        return f"Floor: {self.curr_floor}\nDirection: {self.direction}\n{self.floors_to_visit}"

    def next(self):
        if self.curr_floor == self.max_floor or self.curr_floor == self.min_floor:
            self.direction *= -1

        if self.floors_to_visit[self.curr_floor - self.min_floor] == 1:
            self.floors_to_visit[self.curr_floor - self.min_floor] = 0
        else:
            self.curr_floor += self.direction

    def called_floor(self, floor_called: int):
        if self.is_valid_floor(floor_called):
            if floor_called != self.curr_floor:
                self.floors_to_visit[floor_called - self.min_floor] = 1
        else:
            print(f"The {floor_called} floor doesn't exist in this building!")

    def pressed_floor(self, floor_pressed: int):
        if self.is_valid_floor(floor_pressed):
            if self.occupancy is True and floor_pressed != self.curr_floor:
                self.floors_to_visit[floor_pressed - self.min_floor] = 1
                # if any(self.floors_to_visit):

        else:
            print(f"The {floor_pressed} floor doesn't exist in this building!")

    def people_in(self):
        if self.direction == 0:
            self.occupancy = True

    def people_out(self):
        if self.direction == 0:
            self.occupancy = False
    