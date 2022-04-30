from tkinter import *
from elevator import Elevator


class Interface:

    def __init__(self, elevator: Elevator):
        self._elevator = elevator

        self.window = Tk()
        self.window.title(self._elevator.type)
        self.window.config(padx=20, pady=20, bg="white")

        self.label_floor = Label(text=f"{self._elevator.curr_floor}", font=("Courier", 20, "bold"), fg="red", bg="black")
        self.label_floor.grid(row=0, column=1, padx=50)
        self.label_available = Label(bg="green", width=1, height=1)
        self.label_available.grid(row=1, column=1)
        self.button_in_out = Button(text="In/Out", command=self._pressed_in_or_out, relief=RAISED)
        self.button_in_out.grid(row=2, column=1)

        self.label_outside = Label(text="Outside buttons", bg="white")
        self.label_outside.grid(row=0, column=0)
        self.label_inside = Label(text="Inside buttons", bg="white")
        self.label_inside.grid(row=0, column=2)

        self.outside_floor_buttons = []
        self.inside_floor_buttons = []
        for floor_num in self._elevator.all_floors():
            command_out = lambda temp=floor_num: self._floor_called(temp, self.outside_floor_buttons[temp])
            button = Button(text=f"{floor_num}", command=command_out)
            button.grid(row=self._elevator.max_floor - floor_num + 1, column=0, padx=30, pady=10)
            self.outside_floor_buttons.append(button)

            command_in = lambda temp=floor_num: self._floor_pressed(temp, self.inside_floor_buttons[temp])
            button = Button(text=f"{floor_num}", command=command_in)
            button.grid(row=self._elevator.max_floor - floor_num + 1, column=2, padx=30, pady=10)
            self.inside_floor_buttons.append(button)

        self.window.mainloop()

    def _floor_called(self, desired_floor: int, outside_floor_button: Button):
        self.label_available.config(bg="red")
        self.window.update()
        if self._elevator.called_floor(desired_floor):
            self._floor_button_action(outside_floor_button)
            self.window.after(1500)
        if self._elevator.occupancy is False:
            self.label_available.config(bg="green")

    def _floor_pressed(self, desired_floor: int, inside_floor_button: Button):
        if self._elevator.pressed_floor(desired_floor):
            self._floor_button_action(inside_floor_button)

    def _floor_button_action(self, floor_button: Button):
        floor_button.config(relief=SUNKEN)
        self.window.update()
        while self._elevator.direction != 0:
            if self._elevator.next():
                self.window.after(1500)
                self.label_floor.config(text=self._elevator.curr_floor)
                self.window.update()
        floor_button.config(relief=RAISED)

    def _pressed_in_or_out(self):
        if self._elevator.occupancy is True:
            self.button_in_out.config(relief=RAISED)
            self._elevator.people_out()
            self.label_available.config(bg="green")
        else:
            self.button_in_out.config(relief=SUNKEN)
            self._elevator.people_in()
            self.label_available.config(bg="red")
