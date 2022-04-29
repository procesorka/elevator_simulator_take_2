from tkinter import *
from elevator import Elevator


class Interface:

    def __init__(self, elevator: Elevator):
        self._elevator = elevator

        self.window = Tk()
        self.window.title("Elevator")
        self.window.config(padx=20, pady=20, bg="white")

        self.label_floor = Label(text=f"{elevator.curr_floor}", font=("Courier", 20, "bold"), fg="red", bg="black")
        self.label_floor.grid(row=0, column=1, padx=50)
        self.label_available = Label(bg="green", width=1, height=1)
        self.label_available.grid(row=1, column=1)
        self.button_in_out = Button(text="In/Out", command=lambda: self._pressed_in_or_out(elevator), relief=RAISED)
        self.button_in_out.grid(row=2, column=1)

        self.label_outside = Label(text="Outside buttons", bg="white")
        self.label_outside.grid(row=0, column=0)
        self.label_inside = Label(text="Inside buttons", bg="white")
        self.label_inside.grid(row=0, column=2)

        self.outside_floor_buttons = []
        self.inside_floor_buttons = []
        for i in elevator.all_floors():
            command_out = lambda i=i: self._floor_called(i, self.outside_floor_buttons[i])
            button = Button(text=f"{i}", command=command_out)
            button.grid(row=elevator.max_floor - i + 1, column=0, padx=30, pady=10)
            self.outside_floor_buttons.append(button)

            command_in = lambda i=i: self._floor_pressed(i, self.inside_floor_buttons[i])
            button = Button(text=f"{i}", command=command_in)
            button.grid(row=elevator.max_floor - i + 1, column=2, padx=30, pady=10)
            self.inside_floor_buttons.append(button)

        self.window.mainloop()

    def _floor_called(self, desired_floor: int, outside_floor_button: Button):
        if self._elevator.called_floor(desired_floor):
            outside_floor_button.config(relief=SUNKEN)
            if not self._elevator.next():
                outside_floor_button.config(relief=RAISED)

    def _floor_pressed(self, i, button):
        pass

    def _pressed_in_or_out(self, elevator):
        pass
